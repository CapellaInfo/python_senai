import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('images/formas.jpg')

# Converter a imagem para escala de cinza

# Aplicar uma limiarização para segmentar as formas
_, imagem_binaria = cv2.threshold(imagem, 240, 255, cv2.THRESH_BINARY)

# Encontrar contornos na imagem binária
contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar os contornos na imagem original
cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)

# Mostrar a imagem com os contornos das formas
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Contornos das Formas')
plt.axis('off')

plt.show()