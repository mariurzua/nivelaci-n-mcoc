# 0 minutos y 29 segundos

# Se aprende a, dada una lista (en este caso de palabras), formar un ciclo que recorre la lista. Esto
# se logra mediante el uso del ciclo "for", que recorre la lista y opera con cada elemento de ella.

a = ["platano", "manzana", "microsoft"] #creacion lista de palabras, usando las comillas.

print (a[0])                            #impresion primer elemento de la lista, en posicion 0.
print (a[1])                            #impresion segundo elemento de la lista, en posicion 1.
print (a[2])                            #impresion tercer elemento de la lista, en posicion 2.

for element in a:                       #creacion de un cilo mediante "for". Recorre cada elemento de lista "a".
    print(element)                      #operacion dentro del ciclo for, impresion de cada elemento de lista "a".
    
# 1 minuto y 22 segundos

for element in a:           #creacion de un cilo mediante "for". Recorre cada elemento de lista "a".
    print(element)          #operacion 1 dentro del ciclo for, impresion de cada elemento de lista "a". 
    print(element)          #operacion 2 dentro del ciclo for, impresion de cada elemento de lista "a".
    
# Aqui es posible notar, que para las operaciones dentro de un mismo ciclo "for", se da que se ejecutan
# todo lo que opera dentro del "ciclo for" para el primer elemento. Asi despues se continua con los demas
# elementos de la lista. 
