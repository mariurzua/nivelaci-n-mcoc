# 4 minutos y 19 segundos

# Se aprende a, considerando el diccionario creado anteriormente con los nombres y las edades,
# recorrerlo mediante un ciclo que en el video se busco en internet. Este ciclo es capaz de 
# recorrer tanto la llave como el valor descrito dentro del diccionario.

d = {}                             #creacion de diccionario "d"
# d = {"Juan":24, "Pedro": 36}     
d["Juan"] = 24                     #valor llave "Juan", con valor de 24. Es parte del diccionario
d["Pedro"] = 36                    #valor llave "Pedro", con valor de 36. Es parte del diccionario
d["Pablo"] = 10                    #valor llave "Pablo", con valor de 10. Es parte del diccionario


for llave, valor in d.items():    #ciclo que recorre en diccionario
	print("llave:")               #impresion palabra "llave"
	print (llave)                 #impresion de la llave (lo busca en diccionario)
	print("valor:")               #impresion palabra "valor"
	print(valor)                  #impresion de valor asociado a la llave (lo busca en diccionario)
	print("")                     #impresion de un espacio terminado un ciclo "for"
