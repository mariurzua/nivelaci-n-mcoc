# 12 minutos y 12 segundos

# Se aprendio a generar arreglos con numeros aleatorios, usando rangos, condicionando a enteros o flotantes.

import numpy as np      #importacion libreria numpy

a = np.array([2,3,4], dtype=np.int16)  #creacion matriz "a" con una lista, condicionandola a numeros enteros

print (a)     #impresion matriz "a" definida arriba

print a.dtype   #impresion tipo de elemento matriz "a"

print a.itemsize   #impresion cuanta memoria en bytes toma cada elemento de la matriz 

g = np.random.random((2,3))  #creacion matriz aleatoria de 2 filas y tres columnas (flotantes)
print (g)                    #impresion matriz "g" descrita arriba

t = np.random.randint(0,10,5)  #creacion matriz "t" aleatoria con 5 numeros del 0 al 10
print (t)                      #impresion matriz "t" ya definida

print (t.max())   #impresion numero maximo matriz "t" (aleatorios)


