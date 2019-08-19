#2.54
#En esta parte se aprendio a imprimir un mensaje de texto
print ("hola 1")        
print ("hola 2")

#8.19 - 9.33
#En esta parte se aprendio a comparar 2 numeros segun si uno es mayor o menos que el otro. 
#Para eso se uso el "if" para desencadenar un mìnimo de 1 impresion y un maximo de 3 impresiones 
#dependiendo de si a es mayor o menor que b
a = 3                                       
b = 2
if a < b:
    print ("a es menor que b")
    print ("a es definitivamente menor que b")
print ("no es seguro que a es menor que b")

#9.35 - 11.26
#Aqui se aprendio a usar el "else", el cual se ejecuta cuando no ocurre la condicion dada en el "if"
#Ademas, se pudo aprender en que momento nos encontramos fuera del bloque "if" (bajo el "else")
c = 5
d = 4
if c < d:
    print ("c es menor que d")
else:
    print ("c NO es menor que d")
    print ("No pienso que c es menor que d")
print ("estoy fuera del bloque IF")

#11.27 - 15.00
#Aqui se aprendio a usar el "elif". Este se ejecuta cuando no se cumple la condicion dada por el "if".
#Pueden haber mas de un elif, y solo se ejecutara uno, terminando con el "else" como opcion final
#si no sucede ninguno de los anteriores
e = 20
f = 8
if e < f:
    print("e es menor que f")
elif e == f:
    print ("e es igual a f")
elif e > f + 10:
    print ("e es mayor que f mas 10")
else: 
    print ("e es maypr que 10")
    
#15.10 - 17.12
#Aqui se aprendio que se puede repetir un ciclo "if" y "else" dentro de un "else". 
#Esto se pude usar en reemplazo de el uso de un "elif"
g = 9
h = 8
if g < h:
    print ("g es menor que h")
else:
    if g == h:
        print ("g es igual a h")
    else:
        print ("g es mayor que h")
        
#17.18 - 19.17
#Aqui se aprendio a hacer un programa que analiza si una persona se encuentra en estado de sobrepeso.
#Para ello, se usa el IMC (indice de masa corporal) y se hace un analisis entre el peso (masa en kg)
#y la altura en metros de la persona. Con ese calculo, se compara co 25, y si el IMC es mayor a 25
#la persona en este caso Mari tiene sobrepeso, y si esta bajo, no tiene sobrepeso. Se uso todo 
#aprendido en el curso de "if y else"
nombre = "Mari"
altura_metros = 2
peso_kg = 110

imc = peso_kg / (altura_metros**2)
print ("imc: ")
print (imc)
if imc < 25:
    print (nombre)
    print ("no tiene sobrepeso")
else:
    print (nombre)
    print ("tiene sobrepeso")
