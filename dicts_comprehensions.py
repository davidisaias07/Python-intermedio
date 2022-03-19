
#Asignar variable con llave vacía
#En el rango de 1 al 99 se imprimen los números al cubo
#Que no sean divisibles entre 3
#Se asigna la variable "i" en formato de lista a la variable "my_dict"
#Y se elevado el "i" al cubo

# def run():

#     my_dict = {}

#     for i in range(1,100):
#        if i % 3 != 0:
#         my_dict[i] = i ** 3

#     print(my_dict)     

# run()






#Se coloca "i" como llave, "i**3" como valor
#Misma estructura que en las listas
#Imprime los números al cuadrado de 1 al 100, excepto los divisibles por 3

def run():
    my_dicts = {i: i ** 3 for i in range(1,101) if i % 3 != 0}
    print(my_dicts)


run()