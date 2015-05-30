from random import randint

# Calcualtes the determinant of matrix
def det(matrix):

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    d = 0

    # cofactor expansion across first column
    for i in range(len(matrix)):
        d = d + matrix[i][1] * cofactor(matrix,i,1)

    return d

# Calculate the i,j cofacter of matrix.
# -1 ^ (i+j) * det(minor(matrix, i, j))
def cofactor(matrix, i, j):
    return (-1)**(i + j) * det(minor(matrix,i,j))

# Calculates the i,j minor of matrix.
# That is, the matrix created when row i, column j are
# deleted from matrix
def minor(matrix, i,j):
    A_ij = [[0 for x in range(len(matrix)-1)] for y in range(len(matrix)-1)]

    n = len(matrix)

    for ii in range(i):
        for jj in range(j):
            A_ij[ii][jj] = matrix[ii][jj]

    for ii in range(i+1,n):
        for jj in range(j):
            A_ij[ii-1][jj] = matrix[ii][jj]
    
    for ii in range(i):
        for jj in range(j+1,n):
            A_ij[ii][jj-1] = matrix[ii][jj]

    for ii in range(i+1,n):
        for jj in range(j+1,n):
            A_ij[ii-1][jj-1] = matrix[ii][jj]

    return A_ij

# Creates an n x n matrix of random values
# between 0 and upper, inclusive
def randMatrix(n, upper):
    A = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            A[i][j] = randint(0,upper)

    return A

# Print the elements of matrix in a rectagular form
# The first index in the matrix corresponds to the
# row number in the output; the second index
# corresponds to the column number
def printMatrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            print "%.3d" % matrix[i][j],
        print ""
