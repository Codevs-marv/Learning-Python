"Utiliza todo lo que sabes para generar una lista en una única línea llamada multiples que contenga todos los números múltiples comunes de 2, 3, 4 y 8 entre 0 y 500 (ambos incluidos). No puede contener números repetidos y estos deben estar ordenados de menor a mayor"

multiples = [num for num in range(0,501) if (num%2==0) and (num%3==0) and (num%4==0) and (num%8==0 )]

print(multiples)