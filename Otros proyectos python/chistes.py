import random
import pyjokes

chiste = pyjokes.get_joke(category='all',language='es')
print(f'{chiste}')