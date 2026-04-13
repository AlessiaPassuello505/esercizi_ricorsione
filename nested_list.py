def count_leaf_nodes(input_list):
    if len(input_list)==0:
        return 0

    else:
        counter=0
        for e in input_list:
            #vedo se un elemento è una lista
            if type(e)==list:
                counter+=count_leaf_nodes(e)  #uso metodo ricorsivo
            else:
                counter+=1    #se è una stringa incremento di 1 il counter
        return counter

if __name__=="__main__":
    names= ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names))