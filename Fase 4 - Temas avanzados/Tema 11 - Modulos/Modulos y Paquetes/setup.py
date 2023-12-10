# Este fichero contendrá la configuracion de la instalacion del distribuible

from setuptools import setup


# Definir el distribuible
setup(
    name='Mensajes',
    version='2.0',
    description='Un paquete para saludar y despedir',
    author='Marco Rodriguez',
    author_email='hola@marco.dev',
    url='https://www.marco.dev',
    packages=['Mensajes','Mensajes.Hola','Mensajes.Adios'],
    scripts=['test.py']
)


#> GENERAR EL PAQUETE
# Ingresar por consola el comando: python setup.py sdist

#> INSTALAR EL PAQUETE
# Ingresar por consola el comando: pip install Mensajes-1.0.tar.gz

# Comando: pip list --> Muestra los paquetes que tenemos instalados

#>> ACTUALIZAR VERSION 
# comando: pip install Mensajes-2.0.tar.gz --upgrade

