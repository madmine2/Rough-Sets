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

def extract_between_parentheses(input_string : List[str])-> List[str]:
    pattern = re.compile(r'\((.*?)\)')
    matches = pattern.findall(input_string)
    for match in matches:
        input_string = input_string.replace(f'({match})', '')
    return matches, input_string

def generate_combinations(matrixOfTerms : List[List[str]])->List[List[str]]:
    # Use itertools.product to generate all combinations
    all_combinations = list(product(*matrixOfTerms))
    # Convert each combination tuple to a list
    result = [list(combination) for combination in all_combinations]
    return result

def find_reduct_from_vecteur(vecteur : str)-> List[str]:
    listOfEquivalentTerms, vecteur = extract_between_parentheses(vecteur)
    #print(listOfEquivalentTerms)
    reduct = vecteur.split("&")
    reduct = [item.replace(" ","") for item in reduct]
    reduct = list(filter(None, reduct))
    
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

        #pour la génératio de tous les éléments, on doit transformer la liste reduct en matrice
        matrix = [reduct[i:i+1] for i in range(0, len(reduct))]
        matrixOfTerms= matrixOfTerms + matrix

        #on génère tous les réducts possible, et on n'en renvoie qu'un seul reduct
        allCombinations = generate_combinations(matrixOfTerms)
        reduct = allCombinations[0]
    return reduct
        
    """            # Chaque caractéristique est enregistrée comme un symbole
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
    print(f"sequenceLogique= {sequenceLogique}")
    # Simplifier la séquence logique
    sequenceLogiqueSimplified=simplify_logic(eval(sequenceLogique), form='cnf')
    return str(sequenceLogiqueSimplified)
    """
if __name__ == "__main__" :
    vect = "Polarity & (Charge | Size)"
    find_reduct_from_vecteur(vect)
    pass
