from rembg import remove
from PIL import Image
import io
import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/e/ef/Youtube_logo.png'

print("Descargando imagen desde URL...")
response = requests.get(url)
response.raise_for_status()

print("Abriendo imagen desde bytes...")
input_image = Image.open(io.BytesIO(response.content))

print("Eliminando fondo...")
output_image = remove(input_image)  # devuelve una imagen PIL directamente

print("Guardando imagen...")
output_image.save('imagensinfondo.png')

print("¡Fondo eliminado y archivo guardado!")
