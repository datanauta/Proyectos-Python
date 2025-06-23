def calcular_reading_time_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_from_file = file.read()
    words = text_from_file.split()
    average_reading_speed = 200
    reading_time = len(words) / average_reading_speed

    print(f'El tiempo estimado es {reading_time:.2f} minutos')

if __name__ == '__main__':
    file_path = input('Ingrese la ruta del archivo de texto: ').strip()
    calcular_reading_time_from_file(file_path)
