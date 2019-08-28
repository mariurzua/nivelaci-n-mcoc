# 5 minutos

# Se aprendio a generar una matriz con elementos aleatorios, usando random. Este pide un tope de maximo y un 
# numero para ver cuantos arroja. Esto serviria por ejemplo para un sorteo. 
# Ademas, se aprendio a imprimir los primeros tres elementos, uno en una posicion especifica o el ultimo.

import numpy as np  #importacion libreria numpy

np.random.seed(0)                    #importacion del random         
z1 = np.random.randint(100, size=6)  #creacion mattriz con aleatorios del 0 al 99, y 6 elementos
print (z1)                           #impresion matriz z1

print z1[3]       #impresion cuarto elemento matriz (de los 6 elementos aleatorios)

print z1[0:3]     #impresion primeros 3 elementos de matriz (de los 6 elementos aleatorios)

print z1[-1]      #impresion ultimo elemento matriz (de los 6 elementos aleatorios)
