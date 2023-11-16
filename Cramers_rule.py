

import numpy as np

def Cramer(matrix, solutions):
    '''Takes a numpy matrix and solves for variables given a solution vector'''

    ## Finding the shape of the matrix and finding determinant of main matrix
    shape = matrix.shape
    deter_main = np.linalg.det(matrix)
    
    ## Creating a list of all matrix permutations where each column
    ## is replaced by the solution vector
    permutations = []
    for i in range(shape[1]):
        modify = np.copy(matrix)
        
        ## np.ix_ is an indexing tool where it has the format:
        ## MATRIX[np.ix_([ROWS],[COLUMNS])]
        ## and the rows and columns cannot contain ':' as a catch all
        
        modify[np.ix_(np.arange(0,shape[0]).tolist(),[i])] = solutions
        permutations.append(modify)

    ##Calculating all the associated determinants
    determinants = []
    for i in permutations:
        determinants.append(np.linalg.det(i))

    ## Solving with Cramer's rule and creating a dictionary to return
    variables = {}
    for i in range(shape[0]):
        name = "x" + str(i)
        variables.update({name:(determinants[i]/deter_main)})
    return variables

    
