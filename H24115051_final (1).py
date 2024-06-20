def parse_matrix(matrix_str):   #we first define a function  to  convert the input matrix string into a dictionary representation
    rows = matrix_str.split('|') # we split the input with the seperation of |, within each row are seperated by ,
    matrix = {}
    for i, row in enumerate(rows):
        matrix[i] = list(map(int, row.split(','))) #will be converted into lists of integers reresenting the matrix elements in that row
    return matrix


def multiply_matrices(U, V): #perform matrix multiplication of two matrices represented as dictionaries
    n = len(U)
    M = {} # store result matrix from multiplication

    for i in range(n):
        M[i] = []
        for j in range(n):
            sum_product = 0
            for k in range(n):
                sum_product += U[i][k] * V[k][j]
            M[i].append(sum_product)

    return M


def matrix_to_str(matrix): #this is for converting a matrix dictionary back into string representation
    rows = []
    for i in range(len(matrix)):
        rows.append(','.join(map(str, matrix[i])))
    return '|'.join(rows)


def execute_matrix_multiplication():

    U_str = input("Enter matrix U (rows separated by |, elements separated by ,): ")
    V_str = input("Enter matrix V (rows separated by |, elements separated by ,): ")


    U = parse_matrix(U_str)
    V = parse_matrix(V_str)

    M = multiply_matrices(U, V)


    M_str = matrix_to_str(M)
    print("Resulting matrix M:")
    print(M_str)



execute_matrix_multiplication()# Directly call the function to execute the matrix multiplication
