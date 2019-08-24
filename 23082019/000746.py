# 7 minutos y 46 segundos

# Aqui se aprende con un ejercicio de poder sumar los numeros positivos de una lista,
# a usar el ciclo "for" y ciclo "while". A diferecia de los ejercicios anteriores, 
# se usa el "break", que es como "salir de esto", y se vuelve al inicio del ciclo
# con el siguiente elemento de la lista.

lista_entregada2 = [5, 4, 4, 3, 1, -2, -3, -5]  #creacion lista con negativos y positivos.

total4 = 0                  #creacion variable total4.

for element in lista_entregada2:   #recorriendo la lista entregada con ciclo "for".
    if element <= 0:               #condicion "si el elemento es negativo" no continues.
        break                    #salir de esto. No continua ejecutando
    total4 += element            #acumulacion de la suma de numeros positivos lista.
print (total4)                   #impresion total4, suma numeros positivos.


total5 = 0                          #creacion variable total5.
i = 0                               #creacion variable i con valor 0.

while True:                           #condicion verdadera (redundante).
    total5 += lista_entregada2[i]     #acumulacion de numeros positivos segun posicion variable.
    i += 1                            #aumento variable "i" en una unidad dentro del ciclo "while".
    if lista_entregada2[i] <= 0:      #condicion con "if" que rechaza negativos.
        break                         #salir de esto, no ejecuta mas.
print (total5)                        #impresion total5, suma numeros positivos.
