import time
import os

def beep():
    # En Windows, puedes usar winsound para hacer un beep
    try:
        import winsound
        frequency = 1000  # Hertz
        duration = 500  # milisegundos
        winsound.Beep(frequency, duration)
    except ImportError:
        # Para otros sistemas no Windows, usar print de alerta
        print('\a')

def alarma_con_frase(minutos, segundos):
    total_segundos = minutos * 60 + segundos
    print(f"⏰ La alarma sonará en {minutos} minutos y {segundos} segundos.")
    time.sleep(total_segundos)
    for _ in range(3):
        beep()
        print("¡Alarma activada! Despierta, despierta, despierta.")
        time.sleep(1)

if __name__ == "__main__":
    try:
        minutos = int(input("Ingresa los minutos de la alarma: "))
        segundos = int(input("Ingresa los segundos de la alarma: "))
        alarma_con_frase(minutos, segundos)
    except ValueError:
        print("⚠️ Por favor, ingresa solo números enteros.")
