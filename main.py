import pandas as pd
from make_subsets import make_non_empty_subsets
from rules import make_rules, write_rules
from typing import List, Tuple, Set
#from make_discenibility_matrix_with_labels import make_discernibility_matrix_with_labels
from discernibility import *
from quality_measures import measures

def create_dataframe():
    data1 = { 
        'groupe': ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7'],
        'Age': ['16-30', '16-30', '31-45', '31-45', '16-30', '46-60', '46-60'],
        'Sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'LEMS': ['50+', '0', '1-25', '1-25', '26-49', '26-49', '26-49'],
        'label': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No']
    }
    data2 = {
        'groupe': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        'Polarity': ['Non-polar', 'Non-polar', 'Non-polar', 'Non-polar', 'Polar', 'Polar', 'Polar', 'Polar'],
        'Charge': ['Negative', 'Positive', 'Positive', 'Neutral', 'Negative', 'Negative', 'Neutral', 'Neutral'],
        'Size': ['Small', 'Large', 'Large', 'Large', 'Small', 'Small', 'Large', 'Large'],
        'label': ['Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes']
    }   

    df = pd.DataFrame(data2)
    print(df)
    return(df)


def make_matrix(labels : bool, subsetListFinale: List[Set[int]], df : pd.DataFrame, ensembleFinalKey : Tuple[str, ...], LABEL_DROP, verbose: bool  = False) ->List[List[List[str]]]:
    if labels :
        discernibilityMatrix = make_discernibility_matrix_with_labels(subsetListFinale, df, ensembleFinalKey, LABEL_DROP)
        if verbose :
            print(f"\nMatrice de discernabilité modulo la décision (matrice symmétrique complète): ")
            for element in discernibilityMatrix : 
                print(element)
    else :
        discernibilityMatrix = make_discernibility_matrix( subsetListFinale, df, ensembleFinalKey, LABEL_DROP)
        if verbose :
            print(f"\nMatrice de discernabilité (matrice triangulaire inférieure car symmétrique):")
            for element in discernibilityMatrix : 
                print(element)
            
    sequenceLogiqueSimplified = make_discernibility_function(discernibilityMatrix, ensembleFinalKey)
    #simplifiedDiscernibilityMatrix = make_simplified_discernibility_matrix(discernibilityMatrix, sequenceLogiqueSimplified, ensembleFinalKey)
    if verbose :
        print(f"\nRésultat de la fonction de discernabilité simplifiée = {sequenceLogiqueSimplified}")
        #for element in simplifiedDiscernibilityMatrix : 
        #    print(element)
    return discernibilityMatrix


if __name__ == "__main__" :
    # lecture des données
    csv_file = "grippe.csv"
    #csv_file = "cancer_du_sein.csv"
    data = pd.read_csv(csv_file)
    df = pd.DataFrame(data)

    print(df)
    
    #df = create_dataframe()

    #!!!!!!!!!!!!!!!! CHANGER LE LABEL ET GROUPE-DROP EN FONCTION DU JEU DE DONNEES !!!!!!!!!!!!!!!!
    #nom de la colonne  avec le label: 
    #pour grippe.csv:
    label = 'grypa'
    #pour cancer_du_sein.csv:
    #label = 'V10'

    #on supprime les potentielles données inutiles 
    #(s'il y a par exemple une colonne avec l'id de chaque élément)
    GROUPE_DROP=""
    if GROUPE_DROP:
        df = df.drop(GROUPE_DROP, axis=1)

    # subsets d'inscernabilité
    allSubsetsList, ensembleFinalKey = make_non_empty_subsets(df, LABEL_DROP = label)  
    subsetListFinale = sorted(allSubsetsList[ensembleFinalKey], key=lambda s: min(s))
    print(f"\nSous-ensemble de discernabilité = {subsetListFinale}")
    
    #Matrice de discernabilité:
    #a) sans LABELS (optionnel)
    #simplifiedDiscernibilityMatrix = make_matrix(False,subsetListFinale, df, ensembleFinalKey, label)
    #b) avec LABELS
    simplifiedDiscernibilityMatrixlabels = make_matrix(True,subsetListFinale,df, ensembleFinalKey, label)
    
    rulesDict = make_rules(simplifiedDiscernibilityMatrixlabels, ensembleFinalKey, subsetListFinale)
    #print(f"\nDict = {rulesDict}")

    print("\n===================== SET OF RULES =====================")
    values, ccl = write_rules(rulesDict, df, label)
    (values, ccl)
    
    print("\n===================== QUALITY MEASURES OF EACH RULE =====================")
    for rule in rulesDict:
        supp, strength, accuracy, coverage = measures(df, rulesDict, rule, label)
    
