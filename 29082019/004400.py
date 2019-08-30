# 44 minutos 

# Se aprendio a crear una matriz mas grande, en este caso de 5x5 y a rebanarla de diferentes formas.

import numpy as np    #importacion libreria numpy

a = np.arange(25).reshape(5, 5)   #creacion matriz "a" de 25-1 elementos, 5 filas y 5 columnas.

print (a)   #impresion matriz "a"

y = a[:, 1::3]    #impresion que actua en columnas, desde la columna posicion 1, intercalando en 2 (o sea, me
                  # salta una columna entre medio)
print (y)         #impresion matriz "y" definida arriba

ultimafila = a[4]   #para impresion ultima fila matriz "a"
ultimafila2 = a[-1]   #para impresion ultima fila matriz "a", segunda forma


print (ultimafila)  #impresion ultima fila matriz "a"
print (ultimafila2)  #impresion ultima fila matriz "a", segunda forma

print a[1::2, :3:2]  #impresion en la fila desde posicion 1, intercalando 2 (1 espacio libre) y columnas 0 y 2 (interseccion)
