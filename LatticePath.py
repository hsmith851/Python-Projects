import math

def LatticePath(down, right):
    #Euler Problem Lattice Path
    if (down == 0 or right == 0):
        return 1

    else:
        return LatticePath (down - 1, rigLatticePathht) + LatticePath (down, right - 1)
    #Recursive counting of Lattice Path of NxM Grid
    #LatticePath_v2 uses binomial coefficient of the NxN grid to solve for the number of LatticePath
def LatticePath_v2(down, right):
    numPaths = 0

    return math.factorial (down + right) / (math.factorial (down) ** 2)

print( LatticePath (3, 3))
print (LatticePath_v2 (20, 20))
