import Mensajes.Hola.Saludos

# NOTA:
# Al importar un modulo en otro script, se ejecutarán todas las acciones del modulo importado

# ¿Cómo evitarlo?
# Haciendo uso de comprobaciones dento del modulo importado


# OTRA FORMA DE IMPORTAR

from Mensajes.Hola.Saludos import saludar  # --> Importar algo especifico
from Mensajes.Hola.Saludos import *  # --> Importar todas las funciones

from Mensajes.Adios.Despedidas import * # --> Importar modulo Adios


# Funciones Modulo Hola
saludar() 
saludo() 


# Funciones Modulo Adios
despedir()
Despedida()