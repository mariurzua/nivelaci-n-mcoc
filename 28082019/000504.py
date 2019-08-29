# 5 minutos y 4 segundos

# Se aprendio, parecido al curso de  nivelacion anterior, a trabajar con arreglos.
# Para ello, se inicio con una lista que se transformo en matriz.
# A esa matriz, se le aplico la funcion arange, linspace, reshape, size, shape, como 
# se explica abajo. Tambien se aprendio a ver la memoria en bytes que toma un elemento de la matriz. 

import numpy as np      #importacion libreria numpy

a = np.array([2,3,4])    #creacion matriz "a" con una lista
print (a)                #impresion matriz "a" de tres elementos

b = np.arange(1,12,2)    #creacion matriz con RANGO del 1 al (12-1), cada dos numeros
print (b)                #impresion matriz "b" definida arriba

c = np.linspace(1,12,6)  #creacion matriz "c", del 1 al 12, con 6 elementos separados en igual cantidad
print(c)                 #impresion matriz "c", resulta con flotantes debido a los requerimientos

c1 = c.reshape(3,2)  #reshape pesca la matriz, y realiza remodelacion de puntos. En este caso 3 filas y 2 columnas
                     #la variable c1 la agregamos para que se guarden los cambios.
print (c1)           #impresion matriz "c1", con cambios definidos arriba

print c1.size  #impresion numero de elementos de matriz c1

print c1.shape  #impresion largo de filas y columnas

print c1.dtype  #impresion tipo de elemento de c1 (flotante)

print c1.itemsize  #cuanta memoria en bytes toma cada elemento de la matriz 



