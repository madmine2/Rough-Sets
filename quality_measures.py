import pandas as pd

def measures (donnees : pd.DataFrame, rules):

    column_names = donnees.columns.tolist()
    num_rows, num_columns = donnees.shape

    #calcul support
    supp = 0
    for i in range(num_rows):
        if rules is True: #si l'élément respecte la règle (et la condition et la conclusion)
            supp += 1

    strength = supp/num_rows

    phi = 0 
    for i in range(num_rows):
        if condition(column_names) is True:
            phi += 1
    accuracy = supp/phi

    U_v = 0
    for i in range(num_rows):
        #si la conclusion de la règle est la même que le label
            U_v +=1
    coverage = supp/U_v



    return supp, strength, accuracy, coverage
