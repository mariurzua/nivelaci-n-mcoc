# 11 minutos y 41 segundos

# Se aprendio a multiplicar, sumar, y ordenar los numeros de una matriz. Tambien a trasponerla.

import numpy as np  #importacion libreria numpy
from skimage import io   #importacion io para leer la foto
import matplotlib.pyplot as plt  #importacion para que salga la imagen

 
a_array = np.array([1,2,3,4,5])    #creacion matriz mediante transformacion de una lista
b_array = np.array([6,7,8,9,10])   #creacion matriz mediante transformacion de una lista

suma = (a_array + b_array)        #suma de dos matrices
print(suma)                       #impresion "suma" que es una matriz

mult = (a_array * b_array)      #mult de dos matrices
print (mult)                    #impresion "mult" que es una matriz

print a_array*10            #impresion matriz "a_array" mult por 10

plt.imshow(foto[:,:,0].T)  #el .T intercambia filas y columnas, traspone

x = np.array([2,1,4,3,5])   #creacion matriz con una lista desordenada
np.sort(x)                  #ordena la matriz orden menor a mayor 
print x                     #impresion matriz "x"
