import cv2

camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("❌ No se pudo acceder a la cámara.")
else:
    print("✅ Cámara detectada correctamente.")

camara.release()
