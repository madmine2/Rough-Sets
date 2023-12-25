import pandas as pd
from typing import List, Tuple, Set
from sympy import symbols, Or, And
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic
from utils import make_sequence_logique

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
    symboles = symbols(ensembleFinalKey)
    # Chaque caractéristique est enregistrée comme un symbole
    print(discernibilityMatrix)

    '''
    i = 0
    for ligne in discernibilityMatrix: 
        print(i)
        i+=1
        j=0
        for element in ligne :
            print(j)
            j+=1 
            if element != [] :
                print("test")
                print(element)
                elementTuple = tuple(element)
                setOfEntries.add(elementTuple)'''
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
    #make_discernibility_function(discernibilityMatrix)
    pass