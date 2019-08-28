#2 minutos y 3 segundos

# Se aprendio a cambiar la forma de una matriz de ceros a 2 diferentes.

import numpy as np  #importacion libreria numpy

z = np.zeros(10)          #creacion matriz "z" poblada por ceros, 10 elementos
print(z)                  #impresion matriz "z"

b = z.shape               #creacion de "b" que cambia la forma de la matriz , 
                          #en este caso, arroja el numero de elementos nomas (longitud)

print (b)                 #impresion matriz "b"

z.shape = (10,1)    #creacion matriz "10 filas y una columna" de ceros (modifica a matriz "z")

print(z)            #impresion nueva matriz z
