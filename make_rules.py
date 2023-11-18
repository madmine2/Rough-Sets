import pandas as pd
import numpy as np
from typing import List, Tuple, Set, Dict
from sympy import symbols, Or, And
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic
from utils import make_sequence_logique, find_reduct_from_vecteur
from constant import *

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

def make_rules(discernibilityMatrix : List[List[List[str]]], ensembleFinalKey : Tuple[str, ...],listOfSubsets : List[Set[int]]) -> Dict[int, List[str]] :
    rulesDict= {}
    # Pour chaque colonne de la matrice de discernabilité
    for i, colonne in enumerate(discernibilityMatrix) : 
        # On crée le vecteur logique simplifié de la matrcie
        vecteur = make_discernibility_vector(colonne,ensembleFinalKey)
        # On trouve un des reducts possibles à partir de ce vecteur (ex : vecteur logique = A & (B | C) => reduct possible = {A,B})
        reduct = find_reduct_from_vecteur(vecteur)
        numeroSubset = min(listOfSubsets[i])
        # On associe le reduct au subset correspondant à la colonne        
        rulesDict[numeroSubset] = reduct
    return rulesDict
    
def write_rules(rulesDict, donnees : pd.DataFrame):
    print(donnees)
    valueDict = {}
    cclDict = {}
    for rule in rulesDict: 
        print(f"rule '{rule}'")
        attributes = rulesDict[rule]
        valueAttribute = []
        ccl = donnees.loc[rule, LABEL]
        
        for attribute in attributes:
            valueAttribute.append(donnees.loc[rule, attribute])
        
        # Vérification de la longueur des listes
        if len(attributes) == len(valueAttribute):
            # Création de la chaîne formatée
            conditions = " AND ".join([f"{a} = {b}" for a, b in zip(attributes, valueAttribute)])
            resultat = f"IF {conditions}, THEN {LABEL} = {ccl}"
            valueDict[rule] = valueAttribute
            cclDict[rule] = ccl
            # Affichage du résultat
            print(resultat)

    return valueDict, cclDict

if __name__ == "__main__" :
    #make_discernibility_function(discernibilityMatrix)
    pass