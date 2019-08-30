# 15 minutos y 28 segundos 

# Se aprendio a identificar los tipos de elementos, un int o una tupla. Tambien se aprendio a aplicar 
# operaciones tales como seno, multiplicacion por una constante, etc. Ademas se aprendio a cambiar
# un elemento, indicando su posicion e igualando al nuevo valor. Tambien que el codigo es capaz de cortar
# la parte de un decimal si este pertenece a tipo int.

# a los 22 minutos y 14 segundos, se hace un ejercicio que demuestra que basta con que un elemento de la matriz
# sea flotante, para que la matriz se considere de tipo flotante. Asi mismo, si un elemento es complejo,
# se considera una matriz compleja.

import numpy as np    #importacion libreria numpy

f = 5            #creacion varibale "f"
print (type(f))  #impresion tipo variable "f", un int

r = (5,6)        #creacion varibale "r"
print (type(r))  #impresion tipo variable "r", un tuple

a = np.array([1,2,3,4])    #creacion matriz "a"
print (a)                  #impresion matriz "a"

b = np.array([10,11,12,13])    #creacion matriz "b"
print (b)                  #impresion matriz "b"

print (a*200)    #impresion matriz "a" mult por contante 200

print (np.sin(a))    #imrpime matriz seno de "a" (a cada elemento)

a[0] = 500    #cambio elemento posicion 0 matriz "a" a elemento 500 (int)
print(a)      #imprime nueva matriz "a"

a[1] = 5.7   #cambio elemento posicion 1 matriz "a" a elemento 5.7 (float)
print (a)    #imprime nueva matriz "a", CON LA PARTE DECIMAL DE 5.7 (FLOTANTE) CORTADA, o sea, solo un 5

