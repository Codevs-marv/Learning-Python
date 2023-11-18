# La clase es como un molde para crear objetos


# >>> I N S T A N C I A C I O N <<< #
# Crear un objeto a partir de su clase
class Galleta():
    pass

una_galleta = Galleta() 
otra_galleta = Galleta() # --> objeto de clase galleta

type(una_galleta) # --> __main__.Galleta




# >>> A T R I B U T O S  <<< #
class Galleta_Noel():
    pass

galleta_salada = Galleta_Noel()
galleta_salada.sabor = 'Salado'
galleta_salada.color = 'Beige'
print(galleta_salada.sabor) # ---> salado


class Galletas():
    chocolate = False

galleta1 = Galletas()
galleta1.chocolate  # -->  False


#>> Especificar atributos de manera eficiente

# MÉTODO: es una función dentro de una clase
# __init__()
# self

class Galletas():
    chocolate = False

    # 1er método
    def __init__(self):
        print('Se acaba de crear una galleta')

    # 2do método
    def chocolatear(self):
        self.chocolate = True
    
    # 3er método
    def tiene_chocolate(self):
        if (self.chocolate):
            print('Galleta con chocolate :)')
        else:
            print('Galleta sin chocolate :(')

g = Galletas()
g.tiene_chocolate() # --> Galleta sin chocolate :(
g.chocolatear()
g.chocolate # --> True
g.tiene_chocolate() # --> Galleta con chocolate :)




# Agregar mas Atributos

class Galletas():
    chocolate = False

    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print(f'Se acaba de crear una galleta {sabor} {forma}')

    def chocolatear(self):
        self.chocolate = True
    
    def tiene_chocolate(self):
        if (self.chocolate):
            print('Galleta con chocolate :)')
        else:
            print('Galleta sin chocolate :(')

g = Galletas('salada', 'cuadrada') # se crea un objeto galleta con atributos sabor y forma




# Galleta sin atributos

g = Galletas() # --> genera error (necesita pasarle argumentos)

def __init__(self, sabor=None, forma=None): # valor por defecto None
        self.sabor = sabor
        self.forma = forma

        if sabor != None or forma != None:
            print(f'Se acaba de crear una galleta {sabor} {forma}')
        else:
            print('Se acaba de crear una galleta sin sabor ni forma')

