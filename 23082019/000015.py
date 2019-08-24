# 0 minutos y 15 segundos

# En este codigo es posible ver como se puede realizar una misma operacion mediante el ciclo "for" y medi-
# ante el ciclo "while" (ciclo "for" explicado anteriormente). El ciclo "while" se entiende como "mientras"
# seguido de una condicion. "Mientras ocurra "la condicion" ejecutame lo siguiente". En este caso, la
# suma de los numeros consecutivos del 1 al 4. Para ello, se creo la variable "j", la cual terminada una
# vuelta en el ciclo, cambia su valor segun "+=1". En ciclo frena cuando ya no se cumple la condicion.

total = 0                 #creacion variable para despues modificarla mediante ciclo "for".

for i in range (1, 5):    #creacion ciclo "for", que recorre la "lista" formada con "range".
    total += i            #acumulacion que suma cada elemento de la lista "range(1,5").
print (total)             #impresion del resultado final de "total" terminado el ciclo "for" de recorrer.


total2 = 0           #creacion variable para despues modificarla mediante ciclo "while".
j = 1                #definicion de "j", valor 1 (despues en ciclo "while" esta varia).

while j < 5:         #creacion ciclo "while" que condiciona, entendible como "mientras "j" sea menor que 5".
    total2 += j      #al "total2" inicial, se le suma el valor de "j", mientras cumpla la condicion. 
    j += 1           #variacion de valor de "j", que al terminar el ciclo "while", aumenta en una unidad.
print (total2)       #impresion del resultado final de "total2" terminado el ciclo "while" de recorrer.
