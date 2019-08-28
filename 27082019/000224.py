# 2 minutos y 24 segundos

# Se aprendio a crear una matriz mas extensas con puros 1, identificar su tipo de numero en una posicion dada.

import numpy as np  #importacion libreria numpy

e = np.ones(10)     #creacion matriz "e" de 10 numeros "1"

print(e)            #impresion matriz "e"

print type(e[0])    #impresion tipo de numero en posicion 0 de matriz "e", (un flotante)

f = np.empty(3)     #creacion matriz vacia de 3 elementos

print (f)           #impresion matriz "f"

print type(f[0])    #impresion tipo de numero en posicion 0 de matriz "f", (un flotante)
