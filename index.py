import cv2

imagem = cv2.imread('arquivos/11.jpg', cv2.COLOR_BGR2GRAY) # Importa imagem em escala de cinza

arestas = cv2.Canny(imagem, 30, 200) # Pega arestas da imagem

contours, hierarchy = cv2.findContours(arestas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # Joga contornos da imagem em uma matriz
cv2.drawContours(imagem, contours, -1, (0, 255, 0), 1) # Desenha contornos

print('Larvas encontradas: ' + str(len(contours)))

cv2.imshow("Arestas", cv2.resize(arestas, (800, 600)))
cv2.waitKey(0)

cv2.imshow("Imagem", cv2.resize(imagem, (800, 600)))
cv2.waitKey(0)