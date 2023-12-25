import pandas as pd
import numpy as np
from typing import List, Tuple, Set, Dict
from sympy import symbols, Or, And
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic
from utils import find_reduct_from_vecteur
from discernibility import make_discernibility_matrix, make_simplified_discernibility_matrix, make_discernibility_matrix_with_labels, make_discernibility_function, make_discernibility_vector

def make_rules(discernibilityMatrix : List[List[List[str]]], ensembleFinalKey : Tuple[str, ...],listOfSubsets : List[Set[int]]) -> Dict[int, List[str]] :
    rulesDict= {}
    for i, ligne in enumerate(discernibilityMatrix) : 
        vecteur = make_discernibility_vector(ligne,ensembleFinalKey)
        
        reduct = find_reduct_from_vecteur(vecteur)
        #reduct = make_discernibility_function(vecteur)
        
        numeroSubset = min(listOfSubsets[i])
        # On associe le reduct au subset correspondant à la colonne        
        rulesDict[numeroSubset] = reduct
    return rulesDict

def write_rules(rulesDict, donnees : pd.DataFrame, label):
    valueDict = {}
    cclDict = {}
    for rule in rulesDict: 
        attributes = rulesDict[rule]
        valueAttribute = []
        ccl = donnees.loc[rule, label]

        for attribute in attributes:
            valueAttribute.append(donnees.loc[rule, attribute])
        
        # Vérification de la longueur des listes
        if len(attributes) == len(valueAttribute):
            # Création de la chaîne formatée
            conditions = " AND ".join([f"{a} = {b}" for a, b in zip(attributes, valueAttribute)])
            resultat = f"IF {conditions}, THEN {label} = {ccl}"
            valueDict[rule] = valueAttribute
            cclDict[rule] = ccl
            # Affichage du résultat
            print(f"rule '{rule}': {resultat}")

    return valueDict, cclDict

if __name__ == "__main__" :
    #make_discernibility_function(discernibilityMatrix)
    pass