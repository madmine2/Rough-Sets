import pandas as pd
from typing import List, Tuple, Set
from utils import find_reduct_from_vecteur, make_sequence_logique
from sympy import symbols, Or, And
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic

def make_discernibility_matrix(listOfSubsets : List[Set[int]], donnees : pd.DataFrame, ensembleFinalKey : Tuple[str, ...], LABEL_DROP) -> List[List[List[str]]]: 
    # Préparations du df
    donnees = donnees.drop(LABEL_DROP, axis=1) 
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

def make_discernibility_matrix_with_labels(listOfSubsets : List[Set[int]], donnees : pd.DataFrame, ensembleFinalKey : Tuple[str, ...], LABEL) -> List[List[List[str]]]: 
    # Préparations du df
    column_names = donnees.columns.tolist()
    column_names.remove(LABEL)
    
    # On veut savoir tous les labels uniques qu'ont chaque subsets, on va ajouter tous les labels correspondant aux éléments d'un subset
    # à un set pour n'avoir que les labels uniques 
    listOfSubsetsOfLabels = []
    for subset in listOfSubsets : 
        subsetsOfLabels = set()
        for element in subset : 
            labelTemp = donnees.at[element, LABEL]
            subsetsOfLabels.add(labelTemp)
        listOfSubsetsOfLabels.append(subsetsOfLabels)
        
    # forme la matrice triangulaire en comparant subsets par subsets (groupe1 vs groupe2),
    # si les deux groupes sont les même alors les caractéristiques différentes sont forcément l'ensemble nul.
    # Sinon, en comparant caractéristique par charactéristique et on retient à chaque fois qu'elles sont différentes
    discernibilityMatrix = []
    for i, groupe1 in enumerate(listOfSubsets):
        groupe1 = min(groupe1)
        tempRow = []
        for j in range(len(listOfSubsets)):
            groupe2 = min(listOfSubsets[j])
            tempCell = []
            if groupe1 != groupe2 : 
                # si un des subsets a plus d'un label unique alors forcément, on doit regarder les critéres différents
                if len(listOfSubsetsOfLabels[i]) > 1 | len(listOfSubsetsOfLabels[j]) > 1:
                    for attribute in column_names :  
                            if donnees.at[groupe1, attribute] != donnees.at[groupe2, attribute] :
                                tempCell.append(attribute)
                # Sinon, si le label unique de chaque subset est différent alors on regarde les critères différents
                elif listOfSubsetsOfLabels[i] != listOfSubsetsOfLabels[j]:
                        for attribute in column_names : 
                            if donnees.at[groupe1, attribute] != donnees.at[groupe2, attribute] :
                                tempCell.append(attribute)
                else :
                    pass
            tempRow.append(tempCell)
        discernibilityMatrix.append(tempRow)
    return discernibilityMatrix

def make_simplified_discernibility_matrix(discernibilityMatrix : List[List[List[str]]], sequenceLogiqueSimplified : str,  ensembleFinalKey : Tuple[str, ...]) -> List[List[List[str]]]:
    reduct = find_reduct_from_vecteur(sequenceLogiqueSimplified)
    modified_matrix = [[[item for item in sublist if item in reduct] for sublist in lst] for lst in discernibilityMatrix]
    return modified_matrix

def make_discernibility_function(discernibilityMatrix : List[List[List[str]]], ensembleFinalKey : Tuple[str, ...]) -> str :
    # Chaque caractéristique est enregistrée comme un symbole
    symboles = symbols(ensembleFinalKey)
    # tous les termes répétés entre les "et" peuvent être supprimé, le set permet de supprimer les doublons
    # ex : (a | b) & (a) & (a | b) == (a | b) & (a)  
    setOfEntries = set()
    for ligne in discernibilityMatrix : 
        for element in ligne : 
            if element != [] :
                elementTuple = tuple(element)
                setOfEntries.add(elementTuple)
    # constituer la séquence logique à partir des éléments uniques
    sequenceLogique = make_sequence_logique(setOfEntries, ensembleFinalKey)
    # Simplifier la séquence logique
    sequenceLogiqueSimplified=simplify_logic(eval(sequenceLogique), form='cnf')
    return str(sequenceLogiqueSimplified)


def make_discernibility_vector(discernibilityMatrix : List[List[List[str]]], ensembleFinalKey : Tuple[str, ...], subsetListFinale : List[Set[int]]) -> str :
    # tous les termes répétés entre les "et" peuvent être supprimé, le set permet de le faire automatiquement
    setOfEntries = set()
    #symboles = symbols(ensembleFinalKey)
    # Chaque caractéristique est enregistrée comme un symbole
    print(discernibilityMatrix)

    #pour chaque règle: 
    for i in subsetListFinale: 
        for j in subsetListFinale: 
            element = discernibilityMatrix[i[j]]
            elementTuple = tuple(element)
            setOfEntries.add(elementTuple)
        print(setOfEntries)

    sequenceLogique = ""
    for entrie in setOfEntries : 
        termeTemporaire = "( "
        for t in entrie : 
            position = ensembleFinalKey.index(t)
            termeTemporaire += f"symboles[{position}]"+" | "
        termeTemporaire = termeTemporaire[:-2] + ")"
        sequenceLogique += termeTemporaire + " & "
    sequenceLogique = sequenceLogique[:-2]

    sequenceLogiqueSimplified=simplify_logic(eval(sequenceLogique), form='cnf')
    return str(sequenceLogiqueSimplified) 

if __name__ == "__main__" :
    #make_discernibility_matrix(listOfSubsets , donnees, ensembleFinalKey)
    pass