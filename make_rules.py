import pandas as pd
from typing import List, Tuple, Set
from sympy import symbols, Or, And
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic


def make_rules(discernibilityMatrix : List[List[List[str]]], ensembleFinalKey : Tuple[str, ...]) -> str :
    symboles = symbols(ensembleFinalKey)
    rulesDict= {}
    for ligne in discernibilityMatrix : 
        # tous les termes répétés entre les "et" peuvent être supprimé, le set permet de le faire automatiquement
        setOfEntries = set()
        
        # Chaque caractéristique est enregistrée comme un symbole

    
        for element in ligne : 
            if element != [] :
                elementTuple = tuple(element)
                setOfEntries.add(elementTuple)
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