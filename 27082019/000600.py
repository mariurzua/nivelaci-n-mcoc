# 6 minutos

# Se aprendio, usando una foto JPG, convertir la foto a una matriz de elementos. Luego se jugo con ella
# mediante codigos, pudiendo invertirla en diferentes sentidos segun los codigos descritos, o reducir su tamaño
# o cortarla.

import numpy as np  #importacion libreria numpy
from skimage import io   #importacion io para leer la foto
import matplotlib.pyplot as plt  #importacion para que salga la imagen


foto = io.imread("nosotras.jpg")   #lectura de foto en forma de matriz

tipo = type(foto)      #tipo de foto (da numeros ya que asi se lee como matriz)

print (tipo)           #impresion tipo, asociado a la foto, que son numeros

foto.shape             #conversion de la foto a matriz

print (foto)           #impresion foto como matriz 

plt.imshow(foto)                 #para que muestre la imagen

plt.imshow(foto[::-1])     #esto invierte las filas, osea se invierte la foto en eje X

plt.imshow(foto[:, ::-1])     #esto invierte las columnas, osea se invierte la foto en eje Y

plt.imshow(foto[50:150, 150:280])     #esto hace un recorte en la foto, lo primero las filas y despues las columnas

plt.imshow(foto[::2, ::2])     #reduccion a la mitad del tamaño de la imagen (se ve en los ejes)
