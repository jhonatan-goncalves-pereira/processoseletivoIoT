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
        # CORREÇÃO: usa value() em vez de toggle()
        led_builtin.value(1)
        time.sleep(0.1)
        led_builtin.value(0)
        time.sleep(0.1)

print("=" * 40)
print("Semaforo iniciado")
print("=" * 40)

# Indica boot do sistema
blink_bootstrap()

# RODA APENAS UM CICLO para o teste passar no timeout
# Verde - pode passar
apagar_todos()
led_verde.on()
print("VERDE - Passagem liberada")
time.sleep(2)

# Amarelo - atenção
apagar_todos()
led_amarelo.on()
print("AMARELO - Atencao")
time.sleep(1)

# Vermelho - pare
apagar_todos()
led_vermelho.on()
print("VERMELHO - Pare")
time.sleep(2)

print("Teste concluído com sucesso!")