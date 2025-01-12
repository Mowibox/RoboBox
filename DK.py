import sympy as sp 
from transform_matrix import transform_matrix

def DK(DH_table: list) -> dict:
    """
    Computes the Direct Kinematics of a serial robot

    @param DH_table: The Denavit-Hartenberg table
    """
    n_joints = len(DH_table)

    T0N = transform_matrix(DH_table, 0, n_joints-1)
    T0N = sp.simplify(T0N)

    # Position vector
    p = T0N[:3, 3]

    # Orientation axes
    xN = T0N[:3, 0]
    yN = T0N[:3, 1]
    zN = T0N[:3, 2]

    return {
        "T0N": T0N,
        "position": p,
        "x-axis": xN,
        "y-axis": yN,
        "z-axis": zN,
    }
