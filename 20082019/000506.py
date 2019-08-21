#5 minutos y 6 segundos

#un mapeo
#En este ejemplo, se muestra como se puede definir una funcion con un argumento dentro de ella.
#es posible verlo a traves de la multiplicacion en este caso de (2*x), donde x es el argumento
#variable. A continuacion se llama a la funcion mediante "a" para luego imprimirlo. 

def funcion2(x):                   #definicion de la funcion "funcion2".
    return 2*x                     #retorno de la funcion, dado por una operacion aritmetica (multip).

a = funcion2(3)                    #llamado a la funcion, utilizando la letra "a", con argumento 3.
print (a)                          #impresion de "a", letra que se uso para llamar a la funcion definida.

b = funcion2(6)                    #llamado a la funcion, utilizando la letra "b", con argumento 6.
print (b)

c = funcion2(8)                    #llamado a la funcion, utilizando la letra "c", con argumento 8.
print (c)

#Tambien es posible ver en el minuto 7, que si se llama a la funcion sin indicar un argumento dentro
#del parentesis, tira un error por falta de argumento, ya que por definicion debe existir el argumento.
