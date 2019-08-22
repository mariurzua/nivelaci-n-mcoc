# 8 minutos y 58 segundos

# Aqui se aprende una forma alternativa al minuto 6 del video, para intercambiar dos posiciones de la lista..
# en este caso, se intercambia la posicion 0 con la posicion 2 (primer y ultimo elemento de la lista)



frutas = ["platano", "manzana", "guinda"]    #creacion lista "frutas" con tres elementos (frutas).
print (frutas)                               #impresion lista "frutas".

frutas[0], frutas[2] = frutas[2], frutas[0]  #cambio de elementos mediante uso de sus posiciones.
print (frutas)                                #impresion nueva lista frutas. Se observa intercambio mencionado.
