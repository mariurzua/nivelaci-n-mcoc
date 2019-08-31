# 2 minutos y 44 segundos

# Era un ejercicio en donde agregaban mas de 2 lineas en el mismo grafico, pero debido a que se hace un proceso mecanico y repetitivo, solo hay 2 lineas en el grafico.
# Se aprendio con este ejercicio a graficar distintos datos en forma de ejes coordenados (x,y). 
# Mediante un ejercicio donde el eje "x" eran las edades de la muestras y el eje "y" los salarios de las muestras. 
# Se aprendio a graficar cada linea, darle color, forma, agregarle titulo y leyenda al grafico para hacerlo mas legible. 
# La libreria tambien permitio alterar el diseno del grafico dependiendo de las necesidades, como por ejemplo hacerlo 
# cuadriculado para apreciar los cortes con los ejes de mejor manera.

from matplotlib import pyplot as plt #importacion de libreria pyplot para graficar
plt.style.use("fivethirtyeigth") #distinto estilo al grafico 

de1 = [25,26,27,28,29,30,31,32,33,34,35] # lista de valores para el eje x en el grafico; estas son las edades de programadores
de2 = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752] # lista de valores para el eje y del grafico; cuanto ganan los programadores en promedio
de4 = [45372, 48876, 53850, 57287,63016,65998,70003,70000,71496,75370,83640] #adicion otra lista de salarios



plt.plot(de1,de2, color = k, linewidth = 3, linestyle = "--" , marker =".",label = "Todos los programadores") #se grafico usando los valores de cada lista. Tambien agregamos simbologia para esta linea en el grafico
#se agrego que sea de color negro y una linea discontinua 
#de igual manera con "marker" se agrego que cada punto se marque con un punto
#tambien con "linewidth" se logra que el grosor de la linea sea mayor
plt.plot(de1,de4, "b" ,color = b, linewidth = 3 ,marker = "o", label = "Programadores de Phyton") #se usa los mismos valores de la lista de edades para ambos graficos y se agrega que son otros programadores
#aqui sera de color azul y como ya viene predeterminado, es una linea continua
#agregamos que los puntos se marquen con circulos



plt.xlabel("Edades") #identificacion al eje x, para especificar que son las edades de las personas
plt.ylabel("Salarios (USD") #identificacion al eje y como el salario promedio de cada persona dependiendo de su edad
plt.title("Salario promedio (USD) por edad") #titulo al grafico
plt.tigth_layout() #hace mas exactos las intersecciones
plt.grid(True) #agrega cuadricula al fondo del grafico

plt.show() #impresion grafico
