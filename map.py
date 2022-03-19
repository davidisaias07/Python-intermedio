

def run():

    my_list = [1,2,3,4,5,6,7,8,9]

    #list, map y lambda son obligarios
    #La variable x puede ser cualquier nombre
    #Se coloca luego una coma y la fuente donde se extraen datos
    od = list(map(lambda x: x**2, my_list))
    
    #Rango ejecutado y retorna True o False 
    #Si la division sale par retorna True, sino False
    #for i in od:
    #    print(i % 2 == 0)


    print(od)
run()