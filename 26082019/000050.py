# 0 minutos y 50 segundos

# Se aprendio a crear un diccionario, para luego rellenarlo con informacion. Los diccionarios
# se constituyen por una llave, en este caso escrita dentro de comillas, dos puntos, y la informacion.
# Para este caso se represento la edad de 3 personas, asociada a tres llaves (nombre) 
# como se presenta a continuacion.

d = {}                             #creacion de diccionario "d"
# d = {"Juan":24, "Pedro": 36}     
d["Juan"] = 24                     #valor llave "Juan", con valor de 24. Es parte del diccionario
d["Pedro"] = 36                    #valor llave "Pedro", con valor de 36. Es parte del diccionario
d["Pablo"] = 10                    #valor llave "Pablo", con valor de 10. Es parte del diccionario

print(d["Juan"])                   #impresion informacion asociada a llave "Juan", 24
print(d["Pedro"])                  #impresion informacion asociada a llave "Pedro", 36
print(d["Pablo"])                  #impresion informacion asociada a llave "Pablo", 10


# Es posible notar que si se intenta imprimir una llave que no existe, tira error. ej: "Anastacia"
