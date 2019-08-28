# 9 minutos y 43 segundos

# Se aprendio a condicionar una matriz, imponiendo una condicion (en este caso mayor o menos  a 3), para
# obtener como resultado otra matriz con las palabras True y False dependiendo de si cumple o no la condicion

import numpy as np  #importacion libreria numpy


m = np.array([1,2,3,4,5])    #creacion matriz con una lista de 5 elementos

print (m)                    #impresion matriz "m" creada arriba

menor = m < 3                #variable "menor" refiere a condicion de elemento perteneciente a matriz "m" MENOR a 3

print (menor)               #impresion que arroja nueva matriz, que evalua cada elemento con condicion "menor"

mayor = m > 3                #variable "mayor" refiere a condicion de elemento perteneciente a matriz "m" MAYOR a 3
                             #se da como True si cumple y False si no es asi
print (menor)               #impresion que arroja nueva matriz, que evalua cada elemento con condicion "mayor"
                             #se da como True si cumple y False si no es asi

print m[m>3]    #arroja impresion d ematriz con los mayores a 3 de matriz "m"

