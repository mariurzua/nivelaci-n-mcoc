# 3 minutos y 21 segundos

# Se aprendio en este codigo que, al definir una llave con su valor (En este caso la llave es Juan y el valor 24)
# , se le puede modificar el valor. Al modificarlo, se usa nombrediccionario[llave] = valor, cambiando el valor
# y así, el programa conserva el ultimo valor entregado para la llave.

d = {}                             #creacion de diccionario "d"
    
d["Juan"] = 24                     #valor llave "Juan", con valor de 24. Es parte del diccionario

print(d["Juan"])                   #impresion informacion asociada a llave "Juan", 24

d["Juan"] = 100                    #cambio en la informacion asociada a llave "Juan", ya no es 24 sino 100

print(d["Juan"])                   #impresion nueva informacion asociada a llave "Juan", 100
