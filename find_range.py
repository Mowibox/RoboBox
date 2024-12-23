import sympy as sp

def find_range(J: sp.Matrix) -> list[sp.Matrix]:
    """
    Computes and displays the basis of the image subspace (range) of the Jacobian matrix

    @param J: The Jacobian matrix
    """
    range_J = J.columnspace()

    print("Warning! This result might be wrong, please check by hand if possible.")
    print("Range of the Jacobian:")
    for i, vec in enumerate(range_J, start=1):
        simplified_vec = sp.simplify(vec)
        print(f"Basis vector n°{i}:")
        sp.pprint(simplified_vec)