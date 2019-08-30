# 10 minutos y 18 segundos

# Se aprendio a formar matrices a partir de listas con "array". Tambien se aprendio a usar funciones
# que nos permiten realizar operacion entre matrices. Ademas, se aprendio a usar funciones que nos entregan
# el tipo de elemento, el numero de dimensiones, o una Tupla de la longitud referido a una matriz. 

import numpy as np    #importacion libreria numpy

a = np.array([1,2,3,4])    #creacion matriz "a"

print (a)                  #impresion matriz "a"

b = np.array([10,11,12,13])    #creacion matriz "b"

print (b)                  #impresion matriz "b

print (a+b)   #impresion suma, primer elemento de "a", con primer elemento de "b", y asi...

print(a*b)    #impresion multiplicacion , primer elemento de "a", con primer elemento de "b", y asi...

print (a.dtype)  #imprime tipo de elemento matriz "a"

print (a.ndim)   #imprime numero de dimensiones de "a"

print (a.shape)   #imrpime Tupla longitud de "a"

print (a.itemsize)  #imrpime bytes por elemento
