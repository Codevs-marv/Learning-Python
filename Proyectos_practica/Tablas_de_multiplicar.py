# E J E R C I C I O
# Haz un programa que proporcione las tablas de multiplicar del 1 al 9


for i in range(1,10):
    print(f'Tabla del {i}')
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print()