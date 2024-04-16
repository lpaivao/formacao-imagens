import os
import cv2
import numpy as np

# Função para calcular a porcentagem de pixels que não são pretos em uma imagem em escala de cinza
def calcular_porcentagem_nao_preto(img):
    # Converter para imagem em preto e branco
    _, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    total_pixels = img_bin.shape[0] * img_bin.shape[1]
    print(total_pixels)
    pixels_nao_preto = np.sum(img_bin > 0)  # Conta os pixels que não são pretos (diferentes de 0)
    print(pixels_nao_preto)
    porcentagem_nao_preto = (pixels_nao_preto / total_pixels) * 100
    return porcentagem_nao_preto

# Lista para armazenar as porcentagens
porcentagens = []

# Caminho da pasta de imagens
caminho_pasta = "./imagens/"

# Varre os arquivos na pasta de imagens
for nome_arquivo in os.listdir(caminho_pasta):
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    
    # Verifica se o arquivo é uma imagem (extensão jpg, png, etc.)
    if os.path.isfile(caminho_arquivo) and nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Carregar a imagem em escala de cinza
        imagem = cv2.imread(caminho_arquivo, cv2.IMREAD_GRAYSCALE)
        
        # Mostrar imagem original
        #cv2.imshow('Imagem Original', imagem)
        #\a\\cv2.waitKey(0)
        
        # Calcular porcentagem de pixels que não são pretos
        porcentagem = calcular_porcentagem_nao_preto(imagem)
        
        # Adicionar a porcentagem à lista
        porcentagens.append(porcentagem)
        
        # Exibir a porcentagem
        print("Porcentagem de pixels que não são pretos:", porcentagem)
        
        # Fechar janelas
        cv2.destroyAllWindows()

# Calcular a média das porcentagens
media_porcentagens = np.mean(porcentagens)

# Exibir resultados
print("Porcentagens individuais:", porcentagens)
print("Média das porcentagens:", media_porcentagens)
