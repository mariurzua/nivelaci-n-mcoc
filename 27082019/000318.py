# 3 minutos y 18 segundos 

# Se aprendio a crear matrices con linspace, que pide un rango y una cantidad de elementos para la matriz
# , tambien se identifico el tipo de elemento (flotante) de una posicion en especifico.

import numpy as np  #importacion libreria numpy

h = np.linspace(2,10,5)    #creacion matriz "h", desde el 2 al 10, con 5 elementos

print (h)             #impresion matriz "h" creada arriba

print (type(h[1]))    #impresion tipo de numero en posicion 1 de matriz "h", (un flotante)
