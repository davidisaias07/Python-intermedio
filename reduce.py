from functools import reduce

def run():
    my_list = [2, 2, 2, 2, 2]

   #Brinda 2 elevado a la 5, une todos los caracteres de la lista
   #La "a" y "b" representa a 2 y 2
   #Primer ciclo, "b" se convierte en 4 y se ejecuta nuevamente el ciclo
   #Segundo ciclo, "a" es 4 y "b" es dos

    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print(all_multiplied)

run()