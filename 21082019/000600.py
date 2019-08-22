# 6 minutos

# Aqui se observa como es posible cambiar la posicion de dos elementos en una lista. Esto se logra mediante
# el uso de las posiciones y una nueva variable. 


frutas = ["platano", "manzana", "guinda"]  #creacion lista "frutas" con tres elementos (frutas).
print (frutas)                             #impresion lista "frutas".

temp = frutas[0]                           #"temp" referido a el primer elemento de la lista, el platano.

frutas[0] = frutas[2]                      #primer elemento de la lista, el platano (posicion 0) es reemplazado por
                                           #el tercer elemento de la lista, la guinda (posicion 2).

frutas[2] = temp                           #el tercer elemento de la lista (posicion 2) es reemplazado por
                                           #"temp", quien ya habia sido reemplazado.                   
 
print (frutas)                             #impresion nueva lista frutas. Se observa intercambio mencionado.
