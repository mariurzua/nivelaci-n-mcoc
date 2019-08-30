# 1 hora 27 minutos y 57 segundos

# Se aprendio a hacer un ejercicio donde queriamos imprimir una lista con aquellos numeros dividibles por 3 
# de una matriz de 5x5 enumerada del 1 al 25.
# Para ello, se uso el % que entrega el resto. 

import numpy as np    #importacion libreria numpy

a = np.arange(25).reshape(5, 5)   #creacion matriz "a" de 25-1 elementos, 5 filas y 5 columnas.

print (a)    #impresion matriz 5x5

print (a%3)  #divisible por tres. Si lo es, entrega el resto sobrante. Es una matriz

print (a%3 == 0)  #impresion matriz True False segun si el numero es 0 o no (disivisble)

print (a[a%3 == 0])  #impresion elementos que cumplen la condicion de divisibilidad


output = np.empty_like(a)  #crea matriz de misma forma pero con "basura" (no confiable)
print (output)             #impresion matriz output
