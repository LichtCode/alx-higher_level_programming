def square_matrix_simple(matrix=[]):
    cpy_matrix = [[1,2,3], [2,4,6], [1,3,5]]
    return [list(map(lambda x: x*2, i)) for i in cpy_matrix]
