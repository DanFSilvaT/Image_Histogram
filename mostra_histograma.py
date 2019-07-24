"""
Este código verifica se o sistema Windows tem as dependências que este script precisa para poder correr.
Remove as aspas e este texto para fazer a verificação.

import os

os.system("py -m pip install numpy")
os.system("py -m pip install matplotlib")
os.system("py -m pip install opencv-python")
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
fig = plt.figure(num=None, figsize=(10, 5), dpi=100.45, facecolor=(0.7490, 0.7490, 0.7490), edgecolor='k')



# Abre a imagem ################################################

try:
	"""
	sys.argv[] é uma lista e faz com que este ficheiro .py receba o nome da imagem que lhe foi
	largada em cima. O índice [0] é o caminho para este ficheiro .py e o índice [1] é o
	caminho para a imagem.
	"""
	nome_img = sys.argv[1]
	print("\n" + str(sys.argv[0]) + "\n\nestá a abrir:\n\n" + str(sys.argv[1]))

except:
	"""
	tkinter permite procurar uma imagem através de um UI que serve de explorador do Windows.
	"""
	print('Escolhe uma imagem.')
	
	import tkinter
	janela_raiz = tkinter.Tk()
	janela_raiz.withdraw()
	
	from tkinter.filedialog import askopenfilename
	nome_img = askopenfilename()
	
	print(f'\nA desenhar os histogramas da imagem "{nome_img}".\nAguarda um momento.')
	janela_raiz.destroy()
	
	
img = cv2.imread(f'{nome_img}')



# Converte as cores da imagem para tons de cinza ###############

img_preto_branco = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# Titulo #######################################################

plt.suptitle('Histograma de Imagens')
fig.canvas.set_window_title(nome_img.replace('\\', '/').rsplit('/', 1)[-1])



# Elabora o histograma da luminosidade #########################

plt.subplot(2, 2, 1)
plt.title('Luminosidade')
hist_pb = cv2.calcHist([img_preto_branco], [0], None, [255], [0, 255])
plt.plot(hist_pb, color='k', drawstyle="default", linewidth=0.65, alpha=1.0)
plt.xlim([-1, 255])
plt.ylim([0, (max(hist_pb)*1.05)])
plt.ylabel('Contagem de Pixeis')
plt.xlabel('Tons')



# Elabora os histogramas dos canais individuais RGB ############

num_hist = 2
cor = ('b','g','r')
titulo = ["Azul", "Verde", "Vermelho"]

for canal,col in enumerate(cor):
	"""   (linhas, colunas, caso)   """
	plt.subplot(2, 2, num_hist)
	plt.title(titulo[num_hist-2])
	hist_cor = cv2.calcHist([img],[canal],None,[255],[0,255])
	plt.plot(hist_cor, color = col, drawstyle="default", linewidth=0.65, alpha=1.0)
	plt.xlim([-1, 255])
	plt.ylim([0, (max(hist_cor)*1.05)])
	plt.ylabel('Contagem de Pixeis')
	plt.xlabel('Tons')
	num_hist += 1
	

# Faz a estruturação e mostra os histogramas ###################

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
