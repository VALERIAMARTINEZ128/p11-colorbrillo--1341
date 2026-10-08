 # Ejemplo 1: Conversión entre BGR, RGB y Escala de Grises
# Valeria Yaretzi NC=1341

import cv2
import matplotlib.pyplot as plt

# 1. Cargar imagen del halcón desde disco
# OpenCV la lee en formato BGR
img_bgr = cv2.imread('alcon.jpg')

# Verificar que la imagen se haya cargado correctamente
if img_bgr is None:
    print("ERROR: No se pudo cargar alcon.jpg")
    print("Verifica que alcon.jpg esté en la misma carpeta que este archivo .py")
    exit()

# 2. Conversión BGR -> RGB
# Necesario para visualizar correctamente con Matplotlib
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 3. Conversión BGR -> Escala de grises
# La imagen tendrá un solo canal
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 4. Mostrar los resultados comparativos
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(img_bgr)
axes[0].set_title("Halcón en OpenCV (BGR)")
axes[1].imshow(img_rgb)
axes[1].set_title("Halcón convertido a RGB")

axes[2].imshow(img_gray, cmap='gray')
axes[2].set_title("Halcón en Escala de Grises")

# Quitar los ejes
for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

print("Valeria Yaretzi NC=1341")