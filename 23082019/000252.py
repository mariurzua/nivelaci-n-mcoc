# 2 minutos y 52 segundos

# En este ejemplo, se aprende a usar el ciclo while con el ejercicio de encontrar la suma de nros positivos 
# de la lista. Se puede observar que el valor "i" se relaciona con la posicion, y asi se recorre la lista
# uno por uno, verificando si es (+) o no.


lista_entregada = [5, 4, 4, 3, 1, -2, -3, -5]  #crecion de una lista de de 8 elementos numericos.

total3 = 0     #creacion variable para despues modificarla mediante ciclo "while".

i = 0          #definicio valor inicial "i", usado para indicar posicion en la lista.

while lista_entregada[i] > 0:    #creacion ciclo "while" que condiciona segun lo que sigue, variando posicion.
    total3 += lista_entregada[i]  #al "total3" inicial, se le suma el valor de perteneciente a la posicion
                                  #"i", mientras cumpla la condicion ("lista_entregada[i] > 0").
    i += 1                  #variacion de valor de "i", que al terminar el ciclo "while", aumenta en una unidad.
print (total3)         #impresion del resultado final de "total3" terminado el ciclo "while" de recorrer.

#cabe mencionar que, si la "lista_entregada" tuviera solo los numeros (+), entonces el programa tira un error
#ya que el ciclo "while" incluye el aumento de "i" en una unidad, y ese puesto (posicion 5) no existiria.

#el error se puede corregir con una nueva condicion para el ciclo "while", que se observa a continuacion.

while i < len(lista_entregada) and lista_entregada[i] > 0:  #se agrega una nueva condicion (la primera).
    total3 += lista_entregada[i]    ##al "total3" inicial, se le suma el valor de perteneciente a la posicion
                                  #"i", mientras cumplan ambas condiciones
    i += 1                        #variacion de valor de "i", que al terminar el ciclo "while", aumenta en una unidad
print (total3)                    #impresion del resultado final de "total3" terminado el ciclo "while" de recorrer.
