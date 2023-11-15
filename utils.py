from typing import List, Tuple, Set
import re
import pandas as pd
from itertools import product


def make_sequence_logique(setOfEntries : Set[Tuple[str]], ensembleFinalKey :Tuple[str, ...] )-> str :
    sequenceLogique = ""
    for entrie in setOfEntries : 
        termeTemporaire = "( "
        for t in entrie : 
            position = ensembleFinalKey.index(t)
            termeTemporaire += f"symboles[{position}]"+" | "
        termeTemporaire = termeTemporaire[:-2] + ")"
        sequenceLogique += termeTemporaire + " & "
    sequenceLogique = sequenceLogique[:-2]
    return sequenceLogique

def extract_between_parentheses(input_string : str)-> List[str]:
    pattern = re.compile(r'\((.*?)\)')
    matches = pattern.findall(input_string)
    return matches

def generate_combinations(matrixOfTerms : List[List[str]])->List[List[str]]:
    # Use itertools.product to generate all combinations
    all_combinations = list(product(*matrixOfTerms))
    # Convert each combination tuple to a list
    result = [list(combination) for combination in all_combinations]
    return result

def find_reduct_from_vecteur(vecteur : str)-> List[str]:
    listOfEquivalentTerms = extract_between_parentheses(vecteur)
    reduct = vecteur.split("&")
    reduct = [item.replace(" ","") for item in reduct]
    # Si il y a des "ou" dans l'expression logique simplifiée, alors il faut calculer toutes les 
    # Combinaisons possibles de reduct.
    # Ex : (Age | Sex) & LEMS - > reduct 1 = Age & LEMS et reduct2 = Sex & LEMS
    if len(listOfEquivalentTerms) > 0 :
        matrixOfTerms = []
        for terms in listOfEquivalentTerms : 
            listOfTerms = terms.split("|")
            listOfTerms = [item.replace(" ","") for item in listOfTerms]
            listOfTerms = [item.replace("(","") for item in listOfTerms]
            listOfTerms = [item.replace(")","") for item in listOfTerms]
            matrixOfTerms.append(listOfTerms)
        matrixOfTerms= matrixOfTerms + reduct
        allCombinations = generate_combinations(matrixOfTerms)
        # renvoye qu'un seul reduct
        reduct = allCombinations[0]
    return reduct
        
       
        
        