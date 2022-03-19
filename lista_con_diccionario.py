def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo","lastname": "Martinez"}

    super_list = [
        {"firstname": "Facundo","lastname": "Martinez"},
        {"firstname": "Pablo","lastname": "Malagua"},
        {"firstname": "Marco","lastname": "Perez"}        
    ]

    super_dicts = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums":[1.2,4.5,6.4]
    }

    #Cuando es una lista, en el for solo es una condición
    
    for item in super_list:
        print("Su nombre es: "+item["firstname"] , "y su apellido es:",item["lastname"])

run()