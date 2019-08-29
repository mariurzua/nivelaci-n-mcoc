# 18 minutos y 50 segundos

# Se aprendio en este codigo a trabajar con variaciones del random, suffle que mezcla, choice que da uno al
# azar y integers, que permite un rango y un numero de cuantos debe elegir al azar. 

import numpy as np      #importacion libreria numpy

a = np.arange(10)  #creacion matriz del 0 al (10-1)

print (a)     #impresion matriz "a"

b = np.random.shuffle(a)    #creacion nueva matriz con numeros mezclados

print (b)    #impresion matriz "b"

print np.random.choice(a)  #impresion numero al azar matriz "a"

f = np.random.random_integers(5,10,2)  #aleatorios del 5 al 10, que tire 2

print (f)    #impresion matriz "f"
