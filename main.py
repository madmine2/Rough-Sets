import pandas as pd
from make_subsets import make_non_empty_subsets
from make_discernibility_matrix import make_discernibility_matrix, make_simplified_discernibility_matrix
from make_discernibility_function import make_discernibility_function
from make_discenibility_matrix_with_labels import make_discernibility_matrix_with_labels
from io import StringIO

def create_dataframe():
    data1 = {
        'groupe': ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7'],
        'Age': ['16-30', '16-30', '31-45', '31-45', '16-30', '46-60', '46-60'],
        'Sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'LEMS': ['50+', '0', '1-25', '1-25', '26-49', '26-49', '26-49'],
        'label': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No']
    }
    data2 = {
    'groupe': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Polarity': ['Non-polar', 'Non-polar', 'Non-polar', 'Non-polar', 'Polar', 'Polar', 'Polar', 'Polar'],
    'Charge': ['Negative', 'Positive', 'Positive', 'Neutral', 'Negative', 'Negative', 'Neutral', 'Neutral'],
    'Size': ['Small', 'Large', 'Large', 'Large', 'Small', 'Small', 'Large', 'Large'],
    'label': ['Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes']
    }   
     # Les données que vous avez fournies
    data_str = """groupe,Temperature,Migraine,Faiblesse,Nausee,label
    a,haute,oui,oui,non,oui
    a,haute,oui,non,non,oui
    a,normale,non,non,non,non
    a,normale,oui,oui,non,oui
    a,normale,oui,oui,non,non
    a,haute,non,oui,non,oui
    a,haute,non,non,non,non
    a,normale,non,oui,non,non
    a,normale,non,non,oui,non"""

    # Utilisez StringIO pour lire les données à partir d'une chaîne
    df = pd.read_csv(StringIO(data_str))
    #df = pd.DataFrame(data2)
    return(df)

def make_matrix(labels : bool):
    if labels :
       
        discernibilityMatrix = make_discernibility_matrix_with_labels( subsetListFinale, df, ensembleFinalKey)
    else :
        discernibilityMatrix = make_discernibility_matrix( subsetListFinale, df, ensembleFinalKey)
    
    for element in discernibilityMatrix : 
        print(element)
        
    sequenceLogiqueSimplified = make_discernibility_function(discernibilityMatrix, ensembleFinalKey)
    print(sequenceLogiqueSimplified)
    simplifiedDiscernibilityMatrix = make_simplified_discernibility_matrix(discernibilityMatrix, sequenceLogiqueSimplified, ensembleFinalKey)
    for element in simplifiedDiscernibilityMatrix : 
        print(element)
        
        
        
if __name__ == "__main__" :
    # faire le DataFrame
    df = create_dataframe()
    # faire les subsets
    allSubsetsList, ensembleFinalKey = make_non_empty_subsets(df)  
    subsetListFinale = sorted(allSubsetsList[ensembleFinalKey], key=lambda s: min(s))
    print(subsetListFinale)
    #Sans LABELS
    make_matrix(False)
    
    #AVEC LABELS
    make_matrix(True)
    
    
    

        
        
