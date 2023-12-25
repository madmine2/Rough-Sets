import pandas as pd
from typing import List, Tuple, Set
from utils import find_reduct_from_vecteur

def make_discernibility_matrix(listOfSubsets : List[Set[int]], donnees : pd.DataFrame, ensembleFinalKey : Tuple[str, ...]) -> List[List[List[str]]]: 
    # Préparations du df
    donnees = donnees.drop(GROUPE, axis=1)
    donnees = donnees.drop(LABEL, axis=1) 
    column_names = donnees.columns.tolist()
    
    # forme la matrice triangulaire en comparant subsets par subsets (groupe1 vs groupe2),
    # si ils sont les même alors les caractéristiques différentes sont forcément l'ensemble nul.
    # Sinon, en comparant caractéristique par charactéristique et on retient à chaque fois qu'elles sont différentes
    discernibilityMatrix = []
    for i, groupe1 in enumerate(listOfSubsets):
        groupe1 = min(groupe1)
        tempRow = []
        for j in range(i,len(listOfSubsets)):
            groupe2 = min(listOfSubsets[j])
            tempCell = []
            if groupe1 != groupe2 : 
                for attribute in column_names :  
                    if donnees.at[groupe1, attribute] != donnees.at[groupe2, attribute] :
                        tempCell.append(attribute)
            tempRow.append(tempCell)
        discernibilityMatrix.append(tempRow)
    return discernibilityMatrix


def make_simplified_discernibility_matrix(discernibilityMatrix : List[List[List[str]]], sequenceLogiqueSimplified : str,  ensembleFinalKey : Tuple[str, ...]) -> List[List[List[str]]]:
    reduct = find_reduct_from_vecteur(sequenceLogiqueSimplified)
    modified_matrix = [[[item for item in sublist if item in reduct] for sublist in lst] for lst in discernibilityMatrix]
    return modified_matrix


if __name__ == "__main__" :
    #make_discernibility_matrix(listOfSubsets , donnees, ensembleFinalKey)
    pass