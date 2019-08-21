# 8 minutos y 12 segundos
#Aqui se aprende que, al igualar "f" a un llamado de la funcion con un argumento dentro y hacer correr
# el programa, este imprimira lo definido por la funcion SIN EL RETORNO, pues se esta solo llamando
# a la funcion

#Por otro lado, al imprimir a "f", quien ya llamo anteriormente a la funcion, SI SE CONSIDERA EL RETORNO,
#pues "f" ya llamo anteriormente a la funcion.

def funcion4(x):                         #definicion funcion4 con un argumento dentro ("x").
    print(x)                             #impresion del argumento dentro de la funcion4 definida.
    print("todavia en esta funcion")     #impresion de frase que indica que seguimos dentro de funcion4.
    return 3*x                           #retorno de la funcion4 definida, multiplicando argumento por 3.

f = funcion4(4)                          #llamado de la funcion4 definida (mediante "f"), incluyendo argumento "4".

print (f)                                #impresion de f, que retorna la operacion aritmetica.
