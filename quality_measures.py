import pandas as pd

def measures (donnees : pd.DataFrame, rulesDict, ruleNbr, label):
    num_rows, num_columns = donnees.shape
    supp = 0
    phi = 0 
    U_v = 0

    ruleAttributes = rulesDict[ruleNbr]
    for i in range(num_rows): #pour chaque objet
        tempAtt = 1
        for attribute in ruleAttributes: #on vérifie tous les attributs
            objAttribute = donnees.loc[i, attribute]
            ruleAttribute = donnees.loc[ruleNbr, attribute]
            if objAttribute != ruleAttribute: #si un attribut est différent de la condition de la règle, l'objet ne correspond pas à la condition
                tempAtt = 0
        if tempAtt == 1:
            condition = True
            phi += 1
        else:
            condition = False

        objConclusion = donnees.loc[i, label]
        ruleConclusion = donnees.loc[ruleNbr, label]
        if objConclusion == ruleConclusion: 
            conclusion = True
            U_v +=1 
        else:
            conclusion = False

        if condition == True & conclusion == True:
            supp +=1 


    coverage = supp/U_v
    accuracy = supp/phi
    strength = supp/num_rows
    
    print(f"Quality measures of rule n°{ruleNbr}:")
    print(f"support = {supp}, strength = {strength}, accuracy = {accuracy}, coverage = {coverage}\n")
    return supp, strength, accuracy, coverage

if __name__ == "__main__" :
    #make_discernibility_function(discernibilityMatrix)
    pass
