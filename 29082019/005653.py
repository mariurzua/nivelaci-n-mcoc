# 56 minutos y 53 segundos 

# Se aprendio a imprimir los negativos de una matriz. Esto es valido para poder imprimir otras cosas 
# pasando cada elemento por una condicion.

import numpy as np    #importacion libreria numpy

a = np.arange(0,80,10)   #creacion matriz del 0 al 80-1, intercalando en 10
print (a)                #impresion matriz a

indices = [1 ,2 ,-3]    #indices que indican que elementos voy a usar de la matriz por posicion
y = a[indices]          #nueva matriz "y" con posiciones de indices, sacados de matriz a
print (y)

b = np.array([3, -1, -2, 4, -6, 8])  #creacion matriz b

print (b < 0)    #impresion de menos que 0 de matriz b 

negat = (b<0)     #variable negat con numeros bajo 0
print (b[negat])   #impresion negativos matriz b
