def run():

    my_list = [1,2,3,4,5,6,7,8,9]

    #list, filter y lambda obligatorios
    #Filtra los números pares de my_list
    od = list(filter(lambda numero: numero % 2 == 0, my_list))

    print(od)

run()