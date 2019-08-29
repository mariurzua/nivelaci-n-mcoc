# 9 minutos y 23 segundos

# Se aprendio a formar una matriz de dos filas solo con una linea, la cual se hace con una lista
# y las dos filas con parentesis. Tambien se uso la condicion "<", la cual se responde con True or False
# dentro de la matriz. Ademas, se aprendio a imprimir matrices de ceros, unos. 


import numpy as np      #importacion libreria numpy

b = np.array([(1.5,2,3),(4,5,6)])    #creacion matriz "b" multidimensional, que considera una lista con 
print (b)                            #impresion matriz bidimensional "b"

print (b<4)   #imprime True o false en matriz, segun si es mayor o menos a 4 el elemnto en su posicion 

print (b*7)   #imprime cada elemento de matriz "b" por 7 (en forma de matriz)

b *= 8   #multiplica matriz "b" por ocho con SOLO CUATRO CARACTERES (es mas corto), se conserva

print (b)    #impresion nueva matriz "b", multiplicada por 8

b = np.zeros((3,4))   #creacion matriz "b" de puros ceros, 3 filas y 4 columnas (flotantes)
print (b)             #impresion matriz "b" definida arriba

k = np.ones((4,7))    #creacion matriz "k" de puros unos, 4 filas y 7 columnas (flotantes)
print (k)             #impresion matriz "b" definida arriba

