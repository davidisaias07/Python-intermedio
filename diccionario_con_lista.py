


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

    #En el diccionario el for tiene dos condiciones y se coloca el ".items()"
    for key, values in super_dicts.items():
        print(key, "-",values)


run()