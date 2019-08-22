# 9 minutos y 4 segundos

#PRACTICA

#calculo de la suma de todos numeros multiplos de 3 y 5 menores a 100. 

# En este ejercicio de practica, se utilizo lo aprendido anteriormente. Primero se utilizo la lista de 
# los numeros pertenecientes al rango indicado, usando el "range", que crea la lista de numeros consecutivos
# excluyendo al ultimo. Luego, se puso 2 condiciones, dadas por la peticion. Se uso tambien la variable
# "total4" que acumula aquellos numeros que cumplan la condicion.

print (list(range(1,100)))   #creacion y visualizacion de la lista mediante range, con numeros 1 al 99.

total4 = 0                   #creacion variable "total4", donde se acumularan los numeros que cumplan
                             #la condicion del enunciado.

for i in range(1, 100):      #creacion ciclo "for" que recorre la lista de 1 al 99, usando "range"
    if  i % 3 == 0 and i % 5 == 0:  #condicion mediante "if". Aqui, se ponen dos condiciones usando "and"
                                    #con la idea de que se deben cumplir ambas para que el elemento "i"
                                    #perteneciente a la lista formada por "range(1,100)" del ciclor "for"
                                    #continue a la siguiente operacion, de ser sumado al "total4" acumu-
                                    #lativo. 
                                    
        print (i)                   #impresion de cada elemento que cumple ambas condiciones.
        total4 += i                 #operacion que acumula los elementos que cumplen ambas condiciones.

print (total4)                #impresion de el resultado, la suma de los numeros de la lista
                              #que cumplen ambas condiciones.
