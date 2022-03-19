
#Se asigna una lista vacía a squares
#Imprimir los números al cuadrado de 1 al 100
#Se aplica la condicion que no se imprima los divisibles entre 3
#Se añade en squares el conteo de 1 al 100 elevado al cuadrado

# def run():
#     squares = []
#     for i in range(1,101):
#         if i % 3 != 0:
#             squares.append(i**2)
    
#     print(squares)

# run()




#i elevado al cuadrado en el rango de 1 al 100
#Solo imprimir los números al cuadrado pero que no sean multiplo de 3

# def run():
#     squares = [i**2 for i in range(1,101) if i % 3!= 0]
#     print(squares)

# run()




#Solamente se coloca "i" como primer parámetro y se coloca el "==" para hallar la division
#Muestra los multiplos de 36 que son equivalentes al de 4, 6 y 9
#El mínimo comum multiplo de los números es 36, por ende comienza desde 36
#Se usa el valor and para adjuntar todas las condiciones
#Tambien se puede hacer directamente con el "i % 36 == 0"

# def run():
#     #squares = [i for i in range(1,10001) if i % 4 == 0 and i % 6 == 0 and i % 9== 0]
#     squares = [i for i in range(1,10001) if i % 36 == 0]
#     print(squares)

# run()}



def run():

    my_list = [1,2,3,4,5,6,7]

    numeros_al_cuadrado = [i**2 for i in my_list if i % 2 ==0]
    print(numeros_al_cuadrado)

run()