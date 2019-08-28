# 3 minutos y 39 segundos

# Se aprendio a , dada una lista, convertirla en matriz, identificar el tipo de elemento. 
# Tambien se hizo para una lista de dos litas.

import numpy as np  #importacion libreria numpy

y = np.array([10,20])  #creacion matriz con un 10 y un 20

print (y)              #impresion matriz "y"

a_lista = [1,2,3,4,5,6,7]   #creacion lista de nros del 1 al 7
z = np.array([a_lista])     #conversion de la lista a una matriz
print(z)                    #impresion matriz "z"

print type(z)   #para comprobar que tenemos una matriz 

b_lista = [[9,8,7,6,5,4,3], [1,2,3,4,5,6,7]] #creacion lista con 2 listas
d = np.array([b_lista])                      #conversion lista a matriz
print(d)                                     #impresion matriz "d"
