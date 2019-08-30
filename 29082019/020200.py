# 2 horas y 2 minutos

# Se aprendio a usar palabras claves del eje (axis). Para sacar el valor medio de un canal. 
# Para ello se hicieron ejemplos con una matriz de 6 filas y 4 columnas.

import numpy as np    #importacion libreria numpy

h = np.array([1,2,3])   #creacion matriz h de tres elementos
print (h)               #impresion matriz h

print (np.sum(h))       #impresion suma elementos matriz h

# 2 HORAS Y 10 MINUTOS

j = np.arange(24).reshape(6,4)  #matriz hasta 24-1, 6 filas y 4 columnas
print (j)                       #impresion matriz j

print (j.shape)   #longitudes de matriz j

print (j.mean(axis=0).shape)  #valor medio de cada canal asociado a axis 0

print (j.mean(axis=1).shape)  #valor medio de cada canal asociado a axis 1

# Desde las 2 horas con 23 minutos, se hizo un ejemplo que abarco todo lo aprendido en el video
# Este ejemplo considero desde calculos como minimos, maximos, usando loadtxt. Una variedad de datos
# Se interpreto los numeros con la forma de "rebanar" que se aprendio para poder obtener los datos y vientos
# y poder desarollar el ejercicio practico. 
