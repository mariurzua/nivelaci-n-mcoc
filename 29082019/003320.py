# 33 minutos y 20 segundos

# Se aprendio a imprimir diferentes posiciones de la matriz, cortando, intercalando, etc.

import numpy as np    #importacion libreria numpy

a = np. array([10,11,12,13,14])  #creacion matriz de 5 elementos

print (a[1:4])    #impresion elementos del posicion 1 a la posicion (4-1) de la matriz

print (a[1:-3])  #impresion desde posicion 1 incluida, hasta posicion antes de los ultimos 2 numeros (-3)

print (a[:3])    #impresion primeros 3 elementos de la matriz

print (a[-2:])    #impresion ultimos 2 elementos de la matriz

print (a[::2])    #impresion desde el inicio de la matriz, cada dos numeros (intercalando)
