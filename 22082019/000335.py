# 3 minutos y 35 segundos

# Se aprendio a formar una lista mediante la palabra "range". Lo util de esto, es que permite formar 
# listas sin la necesidad de escribir uno por uno cada elemento de ella. Esta palabra crea una especie
# de lista, la cual se da por "range(x,y)", donde se incluye numeros consecutivos enteros desde el numero
# "x", hasta el numero "y", excluyendo al "y". 
# Tambien, se puede observar en la creacion del ciclo "for", que no es necesario colocar "list" para que 
# el ciclo "for" recorra la lista. Ademas, se puede ver que se usa el "+=", simbolo que indica la operacion
# de que se considera la suma del numero anterior (en este caso del total2) mas el numero siguiente de 
# la lista. Es equivalente a poner "total2 = total2 + i" para el ejemplo descrito. 

c = list(range(1,5))   #creacion lista con numeros 1, 2, 3, 4 (sin contar el ultimo numero, 
                       #en este caso 5).
                       
print (c)              #impresion de elementos pertenecientes a la lista "c", formada con "range".

total2 = 0             #creacion variable "total2", que vale inicialmente 0.

for i in range(1,5):   #creacion ciclo "for", que recorre cada elemento de la lista formada por "range".
    print (i)        #impresion de i, elemento perteneciente a la lista.
    total2 += i      #el numero total2 deberia ser la suma del numero anterior del total2 mas el 
                     #el numero siguiente de la lista.
print (total2)       #impresion de total2, que gracias al "+=", es capaz de sumar cada elemento de la lista.
