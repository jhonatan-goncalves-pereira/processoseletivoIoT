"""
Semáforo IoT – FSM Não-Bloqueante
ESP32 + MicroPython | Jhonatan Gonçalves Pereira

Estados: VERDE (3s) → AMARELO (1s) → VERMELHO (3s) → loop
Temporização: ticks_ms() + ticks_diff() (não-bloqueante)
Proteção: WDT com timeout de 8s
"""

from machine import Pin, WDT
import time

# Estados do semáforo
VERDE, AMARELO, VERMELHO = 0, 1, 2

# Duração de cada estado (ms)
DURACAO_MS = {VERDE: 3000, AMARELO: 1000, VERMELHO: 3000}

# Labels para serial/CI
LABELS = {
    VERDE: "VERDE | Passagem liberada",
    AMARELO: "AMARELO | Atencao",
    VERMELHO: "VERMELHO | Pare",
}

# Pinagem dos LEDs (GPIO)
led_verde = Pin(26, Pin.OUT)
led_amarelo = Pin(25, Pin.OUT)
led_vermelho = Pin(33, Pin.OUT)
led_builtin = Pin(2, Pin.OUT)  # bootstrap visual

# Despacho direto: estado → LED
LEDS = {VERDE: led_verde, AMARELO: led_amarelo, VERMELHO: led_vermelho}

# Watchdog: reinicia se o loop travar por >8s
wdt = WDT(timeout=8000)


def apagar_todos():
    """Garante que apenas um LED fique aceso por vez."""
    for led in LEDS.values():
        led.off()


def ativar_estado(estado):
    """Transição atômica: apaga todos → acende o correto → log na serial."""
    apagar_todos()
    LEDS[estado].on()
    print(LABELS[estado])


def blink_bootstrap(n=3):
    """Feedback visual de boot no LED da placa."""
    for _ in range(n):
        led_builtin.toggle()
        time.sleep_ms(100)


# --- Boot ---
print("Teste")  # Validado pelo CI do Wokwi
print("Semaforo iniciado")
blink_bootstrap()

# --- Loop principal (FSM não-bloqueante) ---
estado_atual = VERDE
ultimo_tick = time.ticks_ms()
ativar_estado(estado_atual)

while True:
    wdt.feed()  # Mantém o WDT satisfeito

    decorrido = time.ticks_diff(time.ticks_ms(), ultimo_tick)
    if decorrido >= DURACAO_MS[estado_atual]:
        estado_atual = (estado_atual + 1) % 3
        ultimo_tick = time.ticks_ms()
        ativar_estado(estado_atual)

    time.sleep_ms(10)  # Granularidade do loop (~0.3% de precisão)