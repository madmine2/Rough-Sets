import pandas as pd
from make_subsets import make_non_empty_subsets
from make_discernibility_matrix import make_discernibility_matrix, make_simplified_discernibility_matrix
from make_discernibility_function import make_discernibility_function, make_discernibility_vector


if __name__ == "__main__" :
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
     # Create DataFrame
    df = pd.DataFrame(data2)
    allSubsetsList, ensembleFinalKey = make_non_empty_subsets(df)  
    subsetListFinale = sorted(allSubsetsList[ensembleFinalKey], key=lambda s: min(s))
    print(subsetListFinale)
    discernibilityMatrix = make_discernibility_matrix( subsetListFinale, df, ensembleFinalKey)
    
    for element in discernibilityMatrix : 
        print(element)
        
    sequenceLogiqueSimplified = make_discernibility_function(discernibilityMatrix, ensembleFinalKey)
    print(sequenceLogiqueSimplified)
    simplifiedDiscernibilityMatrix = make_simplified_discernibility_matrix(discernibilityMatrix, sequenceLogiqueSimplified, ensembleFinalKey)
    for element in simplifiedDiscernibilityMatrix : 
        print(element)
    sequenceLogiqueSimplified2 : make_discernibility_vector(discernibilityMatrix, ensembleFinalKey, subsetListFinale)