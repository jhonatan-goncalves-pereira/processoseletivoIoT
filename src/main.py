# SEMAFORO IoT - maquina de estados com temporizacao nao bloqueante
# placa: ESP32 DevKit C v4 | Framework: MicroPython
# autor: Jhonatan Goncalves Pereira

from machine import Pin
import time

# estados
VERDE    = 0
AMARELO  = 1
VERMELHO = 2

DURACAO_MS = {
    VERDE:    3000,
    AMARELO:  1000,
    VERMELHO: 3000,
}

# para saida serial
LABELS = {
    VERDE:    "VERDE - Passagem liberada",
    AMARELO:  "AMARELO - Atencao",
    VERMELHO: "VERMELHO - Pare",
}

# pinos GPIO
led_builtin  = Pin(2,  Pin.OUT)   # indicador de boot
led_verde    = Pin(26, Pin.OUT)
led_amarelo  = Pin(25, Pin.OUT)
led_vermelho = Pin(33, Pin.OUT)

LEDS = {
    VERDE:    led_verde,
    AMARELO:  led_amarelo,
    VERMELHO: led_vermelho,
}

# defs auxiliares
def apagar_todos():
    """desliga todos os LEDs do semaforo simultaneamente"""
    for led in LEDS.values():
        led.off()

def ativar_estado(estado):
    """transita para o estado informado: desliga todos, acende o correto"""
    apagar_todos()
    LEDS[estado].on()
    print(LABELS[estado])

def blink_bootstrap(n=3):
    """pisca o LED built-in n vezes para sinalizar inicializacao do sistema"""
    for _ in range(n):
        led_builtin.value(1)
        time.sleep_ms(100)
        led_builtin.value(0)
        time.sleep_ms(100)

# boot
print("Teste")
print("=" * 40)
print("Semaforo iniciado")
print("=" * 40)
blink_bootstrap()

# --- maquina de estados principal (temporizacao nao-bloqueante) ---
# usando time.ticks_ms() + time.ticks_diff() para nao bloquear a CPU
estado_atual = VERDE
ultimo_tick  = time.ticks_ms()

ativar_estado(estado_atual)

while True:
    agora     = time.ticks_ms()
    decorrido = time.ticks_diff(agora, ultimo_tick)

    if decorrido >= DURACAO_MS[estado_atual]:
        estado_atual = (estado_atual + 1) % 3
        ultimo_tick  = time.ticks_ms()
        ativar_estado(estado_atual)

    time.sleep_ms(10)