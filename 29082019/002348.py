# 23 minutos y 48 segundos
import numpy as np    #importacion libreria numpy

# Se aprendio a formar una matriz con mas de una fila. Para ello se uso dos listas. A esta nueva matriz
# se aprendio a trasponer, sacar dimension, tipo de elemento. Ademas, se aprendio a imprimir un elemento exacto
# de la matriz, (un numero) donde se debe indicar la fila y la columna. Por otro lado, si posicionamos e indicamos
# solo un valor, nos arroja una lista en la posicion indicada. 

c = np.array([[10,11,12],[30,31,32]])  #creacion matriz "c" formada por dos listas
print (c)                              #impresion matriz "c"

print (c.dtype)    #impresion tipo elemento matriz "c"

print (c.ndim)     #impresion dimension de matriz "c", osea, 2 porque son dos listas

print (c.shape)    #impresion de filas y columnas

print (c.T)    #impresion matriz "c" traspuesta

print (c)   #impresion matriz "c"
 
print (c[0,1])  #impresion elemento fila 0 y columna 1

print (c[1])   #impresion elemento 1 de c, o sea, la segunda lista
