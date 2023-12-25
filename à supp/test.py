"""
from itertools import product

def generate_combinations(list_of_lists):
    # Use itertools.product to generate all combinations
    all_combinations = list(product(*list_of_lists))
    
    # Convert each combination tuple to a list
    result = [list(combination) for combination in all_combinations]
    
    return result

# Example
sublists = [['a', 'b', 'c'], ['1', '2'], ['X', 'Y']]

combinations = generate_combinations(sublists)

# Display the result
for combination in combinations:
    print(combination)
from sympy.logic.boolalg import to_cnf, Or, And
from sympy.abc import P, C, S

def simplify_logical_expression(expr):
    # Convertir l'expression en forme normale conjonctive (CNF)
    cnf_expr = to_cnf(expr)
    print(cnf_expr)

    # Extraire les clauses conjonctives de l'expression CNF
    conjunctive_clauses = And(*cnf_expr.args, evaluate=False).args
    print(conjunctive_clauses)

    # Simplifier chaque clause en retirant les disjonctions
    simplified_clauses = []
    for clause in conjunctive_clauses:
        print(f"cause = {clause}")
        simplified_clause = Or(*clause.args, evaluate=False)
        print(simplified_clause)
        simplified_clauses.append(simplified_clause)
        print(simplified_clause)

    # Retourner la conjonction des clauses simplifiées
    return And(*simplified_clauses, evaluate=False)

# Exemple d'utilisation
expr = P & (C | S)
result = simplify_logical_expression(expr)

print(result)"""
# Matrice avec des chaînes de caractères contenant des symboles de citation simple
matrix = [
    ["abc", "'def'", "ghi"],
    ["jkl", "mno", "'pqr'"],
    ["'stu'", "vwx", "'yz'"]
]
print(matrix)
# Suppression des symboles de citation simple dans chaque chaîne
matrix_without_quotes = [[element.replace("'", "") for element in row] for row in matrix]

# Affichage de la matrice sans les symboles de citation simple
for row in matrix_without_quotes:
    print(row)


