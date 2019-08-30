# 1 hra 43 minutos y 32 segundos

# Se aprendio sobre la explicacion de mas dimensiones que no son posibles de ver tan facil visulamente en una matriz
# , en este codigo se ve e efecto de Nan que refiere a algo que no es un numero. (por ej raiz)

#multidimensional

import numpy as np    #importacion libreria numpy

a = np.arange(25).reshape(5, 5)   #creacion matriz "a" de 25-1 elementos, 5 filas y 5 columnas.
print (a)    #impresion matriz 5x5

print (np.nan+6)  #no se calcula como numero 

print (np.sum([1, np.nan, 9]))  #sum, sin señalar que es nan

print (np.nansum([1, np.nan, 9]))  #suma a traves de la matriz que propaga NaNs
