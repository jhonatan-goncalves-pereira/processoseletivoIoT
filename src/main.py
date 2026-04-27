"""
semaforo IoT – FSM Não-Bloqueante
ESP32 + MicroPython | Jhonatan Gonçalves Pereira
"""

from machine import Pin, WDT
import time

# estados do semáforo
VERDE, AMARELO, VERMELHO = 0, 1, 2

# duração de cada estado (ms)
DURACAO_MS = {VERDE: 3000, AMARELO: 1000, VERMELHO: 3000}

# labels para serial/CI
LABELS = {
    VERDE: "VERDE | Passagem liberada",
    AMARELO: "AMARELO | Atencao",
    VERMELHO: "VERMELHO | Pare",
}

# pinagem dos LEDs
led_verde = Pin(26, Pin.OUT)
led_amarelo = Pin(25, Pin.OUT)
led_vermelho = Pin(33, Pin.OUT)
led_builtin = Pin(2, Pin.OUT)  # LED da placa (bootstrap)

# despacho direto: estado -> LED
LEDS = {VERDE: led_verde, AMARELO: led_amarelo, VERMELHO: led_vermelho}

# watchdog: reinicia se travar >8s
wdt = WDT(timeout=8000)


def apagar_todos():
    """garante exclusão mútua: só um LED aceso por vez."""
    for led in LEDS.values():
        led.off()


def ativar_estado(estado):
    """transição atômica: apaga todos → acende correto → log."""
    apagar_todos()
    LEDS[estado].on()
    print(LABELS[estado])


def blink_bootstrap(n=3):
    """Feedback visual de boot no LED built-in."""
    for _ in range(n):
        led_builtin.value(1)
        time.sleep_ms(100)
        led_builtin.value(0)
        time.sleep_ms(100)


# boot
print("Teste")  # Validado pelo CI do Wokwi
print("Semaforo iniciado")
blink_bootstrap()

# loop FSM não-bloqueante
estado = VERDE
ultimo = time.ticks_ms()
ativar_estado(estado)

while True:
    wdt.feed()
    
    if time.ticks_diff(time.ticks_ms(), ultimo) >= DURACAO_MS[estado]:
        estado = (estado + 1) % 3
        ultimo = time.ticks_ms()
        ativar_estado(estado)
    
    time.sleep_ms(10)  # granularidade do loop