# 12 minutos y 22 segundos 

# En este ejercicio, se aprende a recorrer una lista formada por positivos y negativos.
# Yo lo hice mediante un ciclo for, donde es posible añadir cada elemento a una lista
# que cree vacia para asi juntar una lista que cumpla la condicion de que sea negativo
# el numero (o sea, una nueva lista de negativos). Luego, mediante un ciclo while
# sume los elementos de la lista negativa. 

# EJERCICIO
# No necesariamente conozco el contenido de la lista de antemano, pero se que estan ordenados en orden
# descendiente (o igual). Encontrar la suma de todos los numeros negativos. Se puede con while o for.


lista3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]  #creacion lista con numeros positivos y negativos
nuevalista = []                              #creacion "nuevalista" vacia, donde se meteran los negativos.
nuevototal = 0                               #creacion variable que acumulara el total de la suma.
u = 0                                       #creacion variable "u", que aumentara en una unidad para recorrer el ciclo.

for numero in lista3:               #creacion ciclo for que recorre la lista3.
    if numero <= 0:                 #condicion "si el numero es negativo has lo siguiente:"
        nuevalista.append(numero)   #si s negativo, el numero se agrega a la "nuevalista"
print(nuevalista)                   #impresion para corroborar la lita de negativos

listanegativos = nuevalista         #cambio nombre de variable

while u < len(listanegativos):  #"Mientras u (Variable) sea menor al total de elementos
                                #de numeros de la lista, sumalo.
    nuevototal += nuevalista[u]   #se acumula en "nuevototal" la suma de (-), recorre por
                                  #posiciones.
    u += 1                       #aumento variable "u" en una unidad.
    
print (nuevototal)               #impresion respuesta, suma de los negtivos de la lista3.
