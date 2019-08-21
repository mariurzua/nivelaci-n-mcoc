# En este caso, se hizo un convertidor de millas a kilometros mediante la definicion de una funcion
# donde se ingresan las millas y se retorna los km equivalentes.  
def convertidor_millas_a_km(millas):       #definicion funcion que convierte millas a km
    kilometros = 1.609*millas              #operacion que convierte millas a km, toma el argumento
    return kilometros                      #retorno de kilometros equivalentes a millas ingresadas (Arg)

#ejemplo 1 de utilizacion de la funcion definida
convirtiendo = convertidor_millas_a_km(2)    #llamado a la funcion definida
print (convirtiendo)                         #impresion de los km

#ejemplo 2 de utilizacion de la funcion definida
convirtiendo2 = convertidor_millas_a_km(10)  #llamado a la funcion definida
print (convirtiendo2)                        #impresion de los km
