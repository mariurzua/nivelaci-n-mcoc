# 4 minutos y 22 segundos

# Se aprendio a diferenciar la suma de dos listas. Mediante la suma asi escrita a+b con a y b dos listas, 
# se esta sumando a la lista "a" la lista "b", o sea, aumenta el numero de elementos de "a".
# Luego, mediante un ciclo "for" y una lista nueva y vacia, fue posible sumar elementos de ambas listas
# , pero no extendiedo el numero de elementos, sino que sumando el primer nro de la lista "a" con el primero
# de la lista "b" y asi. 

a = [1,2,3,4]      #creacion lista "a" con cuatro elementos
b = [10,11,12,13]  #creacion lista "b" con cuatro elementos

print (a+b)        #impresion suma listas "a+b" (una lista mas grande, de 8 elementos)

l_vacia = []      #lista vacia

for item1, item2 in zip(a,b):    #ciclo "for" que recorre las 2 listas 
	l_vacia.append(item1+item2)   #se añade la suma entre dos  elemento (uno de cada lista) a la lista vacia ()
	                              #considerando las posiciones

print (l_vacia)    #impresion "l_vacia", que gracias al ciclo "for", es de 4 elementos, 
                   #considerando suma entre elementos de ambas listas
