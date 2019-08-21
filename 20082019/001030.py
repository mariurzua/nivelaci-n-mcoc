# 10 minutos y 30 segundos 

# Calculadora IMC
# Se realizo una calculadora que mediante el calculo del IMC determina si una persona tiene sobrepeso
# o no. Para ello, se uso 3 individuos (Juan, su hermano, su primo) y se creo una funcion que calcula
# el IMC de la persona y ademas, determina si posee sobrepeso comparandolo con el 25.
# En este caso se uso tambien lo aprendido en el video anterior del "if and else"
# Es posible notar que, para que se arroje el retorno de la funcion, es necesario primero que todo
# llamar a la funcion antes, en este caso con la palabra "resultado".
# Luego, se imprime esa palabra "resultado", quien llamo a la funcion, para que se ejecute
# incluido el retorno de la funcion.  

nombre1 = "Juan"                  #definicion nombre1 como Juan
Peso1_kg = 90                     #definicion Peso1_kg de Juan       
Altura1_m = 2                     #definicion Altura1_m de Juan

nombre2 = "Hermano de Juan"       #definicion nombre2 como Hermano de Juan
Peso2_kg = 80                     #definicion Peso2_kg de Hermano de Juan
Altura2_m = 1.9                   #definicion Altura2_md de Hermano de Juan

nombre3 = "Primo de Juan"         #definicion nombre3 como Primo de Juan
Peso3_kg = 81                     #definicion Peso3_kg de Primo de Juan
Altura3_m = 1.7                   #definicion Altura3_m de Primo Juan

def calculadora_IMC(nombre, peso_kg, altura_m):    #definicion funcion calculadora_IMC con 3 argum.
    IMC = peso_kg / (altura_m**2)                  #calculo IMC dentro de funcion, usa 2 argum.
    print ("IMC: ")                                #impresion texto "IMC: "
    print (IMC)                                    #impresion del numero IMC gracias a operacion
    if IMC < 25:                                   #condicion para comparacion de IMC con 25 con "if"
        return nombre + " no tiene sobrepeso"      #retorno de la funcion, usa 1 argumento y texto
    else:                                          #uso de "else" para caso que no ocurre "if"
        return nombre + " tiene sobrepeso"         #retorno de la funcion, usa 1 argumento y texto  
  
#llamado a la funcion para los tres individuos
resultado1 = calculadora_IMC(nombre1, Peso1_kg, Altura1_m) #llamado a la funcion definida (sin retorno)
resultado2 = calculadora_IMC(nombre2, Peso1_kg, Altura2_m) #llamado a la funcion definida (sin retorno)
resultado3 = calculadora_IMC(nombre3, Peso1_kg, Altura3_m) #llamado a la funcion definida (sin retorno)

print (resultado1) #impresion funcion definida (con retorno)
print (resultado2) #impresion funcion definida (con retorno)
print (resultado3) #impresion funcion definida (con retorno)
