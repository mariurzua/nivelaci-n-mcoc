# 6 minutos y 2 segundos

print (list(range(1, 8))) #creacion e impresion de una lista mediante "range", que incluye numeros
                          #consecutivos del 1 al 8, exluyendo el 8.
                          
print (4 % 3)  #ejemplo de que el operador "%", entrega el RESTO de la division de los numeros.
print (5 % 3)  #ejemplo de que el operador "%", entrega el RESTO de la division de los numeros.
print (1 % 3)  #ejemplo de que el operador "%", entrega el RESTO de la division de los numeros.
               #en este caso, es posible ver que 1 no se alcanza a divir por 3, por ende el resto es 1.
print (6 % 3)  #ejemplo de que el operador "%", entrega el RESTO de la division de los numeros.
                        
#encontrando la suma de la lista generada, pero solo de los multiplos del 3.
                          
total3 = 0
for i in range(1,8):
    if  i % 3 == 0: 
        total3 += i
print (total3)
