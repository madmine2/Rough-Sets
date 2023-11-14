import pandas as pd
from typing import List, Tuple, Set

def make_discernibility_matrix_with_labels(listOfSubsets : List[Set[int]], donnees : pd.DataFrame, ensembleFinalKey : Tuple[str, ...]) -> List[List[List[str]]]: 
    GROUPE_DROP = "groupe"
    LABEL_DROP = "label"
    donnees = donnees.drop(GROUPE_DROP, axis=1)
    labels = donnees[LABEL_DROP]
    donnees = donnees.drop(LABEL_DROP, axis=1) 
    column_names = donnees.columns.tolist()
    num_rows, num_columns = donnees.shape
    discernibilityMatrix = []
    for i, groupe1 in enumerate(listOfSubsets):
        tempRow = []
        for j in range(i,len(listOfSubsets)):
            groupe2 = listOfSubsets[j]
            tempCell = []
            if groupe1 != groupe2 : 
                for attribute in column_names :  
                    if donnees.at[groupe1, attribute] != donnees.at[groupe2, attribute] :
                        tempCell.append(attribute)
            tempRow.append(tempCell)
        discernibilityMatrix.append(tempRow)
    return discernibilityMatrix


def make_simplified_discernibility_matrix_with_labels(discernibilityMatrix : List[List[List[str]]], sequenceLogiqueSimplified : str,  ensembleFinalKey : Tuple[str, ...]) -> List[List[List[str]]]:
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.replace("(","")
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.replace(")","")
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.replace("|","")
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.replace("&","")
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.replace("  "," ")
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.replace("   "," ")
    sequenceLogiqueSimplified = sequenceLogiqueSimplified.split(" ")
    modified_matrix = [[[item for item in sublist if item in sequenceLogiqueSimplified] for sublist in lst] for lst in discernibilityMatrix]
    return modified_matrix


if __name__ == "__main__" :
    #make_discernibility_matrix(listOfSubsets , donnees, ensembleFinalKey)
    pass