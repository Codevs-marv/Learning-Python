
                    #  >>>  F I C H E R O S  <<<  #

        #> ¿Qué es un fichero?
# Un conjunto de bits almacenados en un dispositivo de memoria persistente, identificado con un nombre, una dirección a la ruta que lo contiene y una extension.


        #> ¿Qué operaciones permite?
# creacion - apertura - cierre - extension



from io import open

texto = 'Una linea con texto\nOtra linea con texto'


# Crear un fichero
fichero = open('fichero.txt','w')
