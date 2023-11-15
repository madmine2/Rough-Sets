import pandas as pd
from typing import List, Tuple, Set
from sympy import symbols, Or, And
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic
from utils import make_sequence_logique, find_reduct_from_vecteur

def make_discernibility_vector(ligne : List[List[str]],ensembleFinalKey : Tuple[str, ...]):
    # tous les termes répétés entre les "et" peuvent être supprimé, le set permet de le faire automatiquement
    setOfEntries = set()
    # Chaque caractéristique est enregistrée comme un symbole
    symboles = symbols(ensembleFinalKey)
    for element in ligne : 
        # garde que les éléments uniques en les mettant dans un set
        if element != [] :
            elementTuple = tuple(element)
            setOfEntries.add(elementTuple)
    # Avec tous les éléments, on fait une expressions logique 
    sequenceLogique = make_sequence_logique(setOfEntries, ensembleFinalKey)
    # et on la simplifie autant que possible
    if len(sequenceLogique) != 0:
        sequenceLogiqueSimplified=simplify_logic(eval(sequenceLogique), form='cnf')
    return str(sequenceLogiqueSimplified)

def make_rules(discernibilityMatrix : List[List[List[str]]], ensembleFinalKey : Tuple[str, ...],listOfSubsets : List[Set[int]]) -> str :
    
    rulesDict= {}
    for i, ligne in enumerate(discernibilityMatrix) : 
        vecteur = make_discernibility_vector(ligne,ensembleFinalKey)
        reduct = find_reduct_from_vecteur(vecteur)
        numeroSubset = min(listOfSubsets[i])
        rulesDict[numeroSubset] = reduct
    
    
    
if __name__ == "__main__" :
    #make_discernibility_function(discernibilityMatrix)
    pass