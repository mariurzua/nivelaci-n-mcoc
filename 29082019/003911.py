# 39 minutos y 11 segundos 

# Se aprendio a, con el uso de una matriz formada por dos listas, imprimir ciertos elementos, dependiendo 
# posiciones, intercalaciones, etc.

import numpy as np    #importacion libreria numpy

a = np. array([[10,11,12,13,14,15],[34,35,36,37,38,39]])  #creacion matriz de 5 elementos

a1 = a[0, 3:5]    #de la posicion 0 (o sea primera lista), imprime del elemento 3 al (5-1)

print (a1)        #impresion descrita arriba 

print (a[:,2])    #impresion elemento en pisicion 2 de cada lista

print (a[1::2,::4])   #impresion lista 2 elementos posicionados en intervalos de 3 espacios libres
