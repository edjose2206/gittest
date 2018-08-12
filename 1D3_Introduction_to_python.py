##1D3:Introduction to python
##Codes used in this class
##Cuando se escribe "python" en la terminal se habilita por asi
##decirlo python en la terminal
##Es necesario descargar los siguientes paquetes con la terminal

sudo apt-get install python-dev ipython python-matplotlib python-numpy python-scipy cython

#Todos son paquetes para python
 
#Al escribir ipython en la terminal se activa un modo que 
#nos permite programar funcuiones de python desde la terminal

import numpy as np ## Nos permite utilizar las funciones de numpy

a=no.array([0,1,2,3,4,5]) ##Creamos un arreglo de datos

a[3] #Nos permite acceder al elemento 3 del arreglo

a[1:3] #Nos permite acceder a los primeros 3 elementos del arreglo

import matplotlib.pyplot as plt ##Nos permite utilizar las funciones de matplotlib

plt.plot(a) #Modifica la variable para que se pueda plotear

plt.show() ##Plotea el valor obtenido anteriormente mediante
#plt.plot(variable)

##Para correr un archivo py desde la terminal ipy se utiliza
##el comnado run nombre_archivo













