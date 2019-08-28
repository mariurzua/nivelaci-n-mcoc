# 10 minutos y 43 segundos

# Considerando la foto anterior, se aprendio a generar cambios dentro de la matriz generada por la foto,
# para ello, se uso "np.where", donde el primer  numero es como "umbral" relacionado con la condicion, 
# el segundo es el reemplazo si esque SI cumple y el tercero si NO cumple.

import numpy as np  #importacion libreria numpy
from skimage import io   #importacion io para leer la foto
import matplotlib.pyplot as plt  #importacion para que salga la imagen

foto_masked = np.where(foto > 50, 255, 0)  #donde la foto es mayor a 50, lo reemplazamos con 255, y sino con 0

plt.imshow(foto_masked)

#se tomo 50 como umbral, y al generar los cambios cambian los colores de la imagen 

