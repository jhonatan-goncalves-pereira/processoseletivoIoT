from machine import Pin
import time

# Definição dos pinos
led_verde = Pin(26, Pin.OUT)
led_amarelo = Pin(25, Pin.OUT)
led_vermelho = Pin(33, Pin.OUT)

def apagar_todos():
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()

print("Teste")
print("Semaforo iniciado")

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