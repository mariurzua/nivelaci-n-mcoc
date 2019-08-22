# Aqui se aprende a usar el "pop". Este sirve, para borrar el ultimo elemento de la lista, ya sea una lista,
# una palabra, o un numero. El "pop" se puede utilizar sin algo dentro de sus parentesis (a diferencia del
# append), ya que automaticament se refiere la eliminacion del ultimo elemento. 

a = [3, 10, -1, 1, "hola", [1, 2]]   #creacion lista "a" con 6 elementos, posiciones 0, 1, 2, 3, 4, 5.
print (a)                            #impresion lista "a"

a.pop()                              #primer recorte ultimo elemento. 

print (a)                            #impresion lista "a". Se observa que ya no esta el ultimo elemento.

a.pop()                              #segundo recorte ultimo elemento. 

print (a)                            #impresion lista "a". Se observa que ya no estan 2 ultimos elementos.
