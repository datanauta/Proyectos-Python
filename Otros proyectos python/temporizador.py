import time

def countdown(minutes):

    total_seconds = minutes *60

    while total_seconds:
        mins,secs = divmod(total_seconds,60)
        time_format = f'{mins:02}:{secs:02}'
        print(time_format)
        time.sleep(1)
        total_seconds -=1
print('Tiempo finalizado')
countdown(2)