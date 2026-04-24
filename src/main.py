from machine import Pin
import time

# LED built-in para indicar que o sistema está vivo
led_builtin = Pin(2, Pin.OUT)

# Definição dos pinos do semáforo
led_verde = Pin(26, Pin.OUT)
led_amarelo = Pin(25, Pin.OUT)
led_vermelho = Pin(33, Pin.OUT)

def apagar_todos():
    """Desliga todos os LEDs do semáforo"""
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()

def blink_bootstrap():
    """Indica que o sistema iniciou com 3 bips no LED built-in"""
    for _ in range(3):
        led_builtin.toggle()
        time.sleep(0.1)
    led_builtin.off()

print("=" * 40)
print("Semaforo iniciado")
print("=" * 40)

# Indica boot do sistema
blink_bootstrap()

while True:
    # Verde - pode passar
    apagar_todos()
    led_verde.on()
    print("VERDE - Passagem liberada")
    time.sleep(3)

    # Amarelo - atenção
    apagar_todos()
    led_amarelo.on()
    print("AMARELO - Atencao")
    time.sleep(1)

    # Vermelho - pare
    apagar_todos()
    led_vermelho.on()
    print("VERMELHO - Pare")
    time.sleep(3)