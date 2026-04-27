"""
Semáforo IoT – Máquina de Estados Finita (FSM) Não-Bloqueante
==============================================================
Placa   : ESP32 DevKit C v4
Firmware: MicroPython
Autor   : Jhonatan Gonçalves Pereira

Descrição
Implementa um semáforo de trânsito simulado usando o padrão FSM
(Finite State Machine) com temporização não-bloqueante via ticks_ms()
e proteção por Watchdog Timer (WDT).

Fluxo de estados (ciclo contínuo)
----------------------------------
  ┌──────────┐  3 s  ┌──────────┐  1 s  ┌──────────┐  3 s
  │  VERDE   │──────▶│ AMARELO  │──────▶│VERMELHO  │──────┐
  └──────────┘       └──────────┘       └──────────┘      │
        ▲                                                  │
        └──────────────────────────────────────────────────┘

Pinagem (GPIO)
--------------
  GPIO  2  → LED built-in (bootstrap)
  GPIO 26  → LED verde    (passagem liberada)
  GPIO 25  → LED amarelo  (atenção)
  GPIO 33  → LED vermelho (parada obrigatória)

Temporização não-bloqueante
----------------------------
  ticks_ms() + ticks_diff() evita time.sleep() no loop principal,
  mantendo o processador disponível para futuras expansões
  (leitura de sensores, botão de pedestre, comunicação MQTT, etc.).

Watchdog Timer
--------------
  WDT(timeout=8000 ms) reinicializa o ESP32 automaticamente caso
  o loop principal trave por qualquer motivo (deadlock, exceção não
  tratada). feed() é chamado a cada iteração (~10 ms).
"""

from machine import Pin, WDT
import time

# ---------------------------------------------------------------------------
# Constantes de estado (int como enum leve para MicroPython)
# ---------------------------------------------------------------------------
VERDE: int    = 0   # passagem liberada – via livre ao tráfego
AMARELO: int  = 1   # atenção – sinal de transição, prepare-se para parar
VERMELHO: int = 2   # parada obrigatória – acesso bloqueado

# Duração de cada estado em milissegundos
# Valores baseados em referências de semáforos urbanos de baixo volume
DURACAO_MS: dict = {
    VERDE:    3000,   # 3 s – tempo mínimo para pedestres cruzarem via simples
    AMARELO:  1000,   # 1 s – transitório rápido (padrão DENATRAN)
    VERMELHO: 3000,   # 3 s – espera mínima segura antes de liberar novamente
}

# Rótulos para saída serial (debug local e evidência de testes no CI)
LABELS: dict = {
    VERDE:    "VERDE    | Passagem liberada",
    AMARELO:  "AMARELO  | Atencao",
    VERMELHO: "VERMELHO | Pare",
}

# ---------------------------------------------------------------------------
# Inicialização de hardware
# ---------------------------------------------------------------------------
# Critérios de seleção dos pinos:
#   GPIO 26 – pino de propósito geral sem função reservada no boot
#   GPIO 25 – DAC1, usado aqui exclusivamente como saída digital
#   GPIO 33 – RTC GPIO, compatível com saída digital e sem conflito UART
#   GPIO  2 – LED built-in do DevKit C v4, usado apenas no boot

led_builtin: Pin  = Pin(2,  Pin.OUT)   # LED azul da placa (bootstrap only)
led_verde: Pin    = Pin(26, Pin.OUT)   # semáforo: verde
led_amarelo: Pin  = Pin(25, Pin.OUT)   # semáforo: amarelo
led_vermelho: Pin = Pin(33, Pin.OUT)   # semáforo: vermelho

# Dicionário de despacho: mapeia estado → pino GPIO diretamente
# Evita if/elif encadeados, mantendo O(1) de acesso e código extensível
LEDS: dict = {
    VERDE:    led_verde,
    AMARELO:  led_amarelo,
    VERMELHO: led_vermelho,
}

# ---------------------------------------------------------------------------
# Watchdog Timer
# ---------------------------------------------------------------------------
# Timeout de 8 s: suficiente para cobrir o estado mais longo (VERDE/VERMELHO
# = 3 s) com ampla margem. O wdt.feed() no loop principal impede o disparo
# em operação normal; em caso de travamento, o ESP32 reinicia sozinho.
wdt: WDT = WDT(timeout=8000)

# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def apagar_todos() -> None:
    """Desliga todos os LEDs do semáforo de forma atômica.

    Centralizar o desligamento aqui garante que nunca dois LEDs
    permaneçam acesos simultaneamente — evita sinais ambíguos que
    poderiam ocorrer em implementações com lógica de transição simples.
    """
    for led in LEDS.values():
        led.off()


def ativar_estado(estado: int) -> None:
    """Realiza a transição completa para o estado informado.

    Fluxo interno
    -------------
      1. apagar_todos()    → estado neutro seguro (nenhum LED aceso)
      2. LEDS[estado].on() → acende o LED correto via despacho direto
      3. print()           → registra transição na serial para debug/CI

    Args:
        estado: constante de estado (VERDE, AMARELO ou VERMELHO)
    """
    apagar_todos()
    LEDS[estado].on()
    print(LABELS[estado])


def blink_bootstrap(n: int = 3) -> None:
    """Pisca o LED built-in n vezes como feedback visual de inicialização.

    Usa time.sleep_ms() porque ocorre uma única vez durante o boot,
    antes do loop principal; o impacto no desempenho é desprezível.

    Args:
        n: número de piscadas (padrão = 3)
    """
    for _ in range(n):
        led_builtin.value(1)   # acende
        time.sleep_ms(100)
        led_builtin.value(0)   # apaga
        time.sleep_ms(100)


# ---------------------------------------------------------------------------
# Boot / Inicialização
# ---------------------------------------------------------------------------
print("Teste")                         # string esperada pelo GitHub Actions CI
print("=" * 40)
print("Semaforo iniciado")
print("=" * 40)

blink_bootstrap()                      # feedback visual de boot completo

# ---------------------------------------------------------------------------
# Loop principal – Máquina de Estados Finita (FSM) não-bloqueante
# ---------------------------------------------------------------------------
#
# Estratégia de temporização:
#   • time.ticks_ms()         → lê o contador de ms (32 bits, wraps ~49 dias)
#   • time.ticks_diff(a, b)   → calcula diferença com tratamento de overflow
#   • time.sleep_ms(10)       → granularidade do loop; mantém uso de CPU < 5 %
#
# Por que não usar time.sleep() diretamente no loop?
#   sleep() bloqueia a CPU pelo tempo total do estado (até 3 s), tornando
#   impossível reagir a eventos externos (botão, sensor, mensagem MQTT).
#   A abordagem com ticks_diff() verifica o tempo decorrido sem bloquear,
#   deixando o processador livre para outras tarefas a cada iteração.

estado_atual: int = VERDE
ultimo_tick: int  = time.ticks_ms()

ativar_estado(estado_atual)            # garante estado inicial explícito e definido

while True:
    # alimenta o WDT a cada iteração — prova que o loop está vivo
    wdt.feed()

    agora: int     = time.ticks_ms()
    decorrido: int = time.ticks_diff(agora, ultimo_tick)

    # verifica se a duração do estado atual foi atingida
    if decorrido >= DURACAO_MS[estado_atual]:
        # avança para o próximo estado em ciclo: 0 → 1 → 2 → 0 → ...
        estado_atual = (estado_atual + 1) % 3
        ultimo_tick  = time.ticks_ms()    # reseta o temporizador do novo estado
        ativar_estado(estado_atual)

    # cede CPU por 10 ms: granularidade de ~0,3 % para estados de 3 s
    time.sleep_ms(10)