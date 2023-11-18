import pandas as pd
from itertools import chain, combinations
from typing import List, Tuple, Set, Dict
from constant import *

def make_non_empty_subsets(donnees : pd.DataFrame) -> Tuple[Dict[str, List[Set[int]]], Tuple[str, ...]]:
    donnees = donnees.drop(GROUPE, axis=1)
    donnees = donnees.drop(LABEL, axis=1) 
    column_names = donnees.columns.tolist()
    num_rows, num_columns = donnees.shape
    # On génére toutes les combinaisons possibles d'associations de groupes
    all_combinations = list(powerset(column_names))
    all_combinations.remove(()) # on retire la combinaison ensemble vide
    allSubsetsDict = {}
    for subsetNumber,subset in enumerate(all_combinations):
        tempDict = {}
        # Pour les sets qui ne contiennent que un élément (autant de tels sets que de caractéristiques)
        # On calcule explicitement les subsets non-vide
        if subsetNumber < (num_columns) :
            subset = subset[0]
            for i in range(num_rows):     
                caracteristiqueValue = donnees.at[i,subset]   
                # si la valeur est déjà dans le dictionnaire, ajoute le groupe au set associé    
                if caracteristiqueValue in tempDict :
                    tempDict[caracteristiqueValue].add(i)
                #sinon crée un nouveau set avec ce groupe
                else :
                    tempDict[caracteristiqueValue] = {i}
            newListeOfSub = list(tempDict.values())
        else : # sinon, on calcule en utilsant les sets déjà fait pour aller plus vite
            #On compare les subsets déjà calculé pour le croisement des n-1 premiers attributs
            firstGroupe = subset[:-1]
            # avec les subsets calculé pour le dernier attribut
            secondGroupe = subset[-1]
            if len(firstGroupe) == 1:
                firstGroupe = firstGroupe[0]
            listOfSubsets1 = allSubsetsDict[firstGroupe]
            listOfSubsets2 = allSubsetsDict[secondGroupe]
            newListeOfSub = []
            # fais l'intersection de chaque subset de la première liste avec chaque subset de la seconde
            for sub1 in listOfSubsets1:
                for sub2 in listOfSubsets2:
                    newSub = sub2.intersection(sub1)
                    # si le set est non vide, alors on l'append
                    if len(newSub) > 0:
                        newListeOfSub.append(newSub)
        # on ajoute la liste de subsets à la clé composée des attributs correspondants
        allSubsetsDict[subset] = newListeOfSub
    return allSubsetsDict, tuple(column_names)
        
            
# fonction qui fait toutes les combinaisons possibles dans une liste d'élèments
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



if __name__ == "__main__" :
    data = {
        'groupe': ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7'],
        'Age': ['16-30', '16-30', '31-45', '31-45', '16-30', '46-60', '46-60'],
        'Sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'LEMS': ['50+', '0', '1-25', '1-25', '26-49', '26-49', '26-49'],
        'label': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No']
    }
    # Create DataFrame
    df = pd.DataFrame(data)
    allSubsetsList, ensembleFinalKey = make_non_empty_subsets(df)
    print(allSubsetsList)