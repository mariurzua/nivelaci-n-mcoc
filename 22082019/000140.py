# 1 minuto y 40 segundos

# Se aprendio a ver como un ciclo "for" opera en una lista de numeros. En el ejemplo es posible ver 
# como se crea una variable llamada "total", donde la idea de esta, es usarla para obtener la suma de 
# los elementos pertenecientes a la lista. Luego, mediante un ciclo "for", se añade a esta variable
# (que inicialmente tendria el valor de cero) la suma de cada elemento. Asi, al recorrer la lista un 
# elemento por un elemento, se da que la variable "total" va aumentando. Finalmente se puede imprimir
# lo que se buscaba, la suma de los elementos pertenecientes a la lista.

b = [20, 10, 5]     #creacion lista con tres elementos, en posiciones 0, 1, 2.
total = 0           #creacion variable "total" equivalente inicialmente a 0.

for e in b:         #creacion ciclo "for", que recorre la lista b.
    print(e)        #operacion dentro del ciclo "for", en este caso, la impresion del elemento.
    
for e in b:             #creacion ciclo "for", que recorre la lista b.
    total = total + e   #operacion dentro del ciclo "for", que agrega al total la suma de cada elemento.
print (total)           #impresion del total nuevo, que sumo cada elemento gracias al ciclo "for"
