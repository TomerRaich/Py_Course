def mat_transpose(mat):
    mat2 = mat[:(len(mat[1])):1]
    for n in range(len(mat[1])):
        mat2[n] = mat[:(len(mat)):]
        for m in range(len(mat)):
            mat2[n][m] = mat[m][n]
    return mat2

mat = [[1,2],[3,4],[5,6]]
mat_T = mat_transpose(mat)
print(mat)
print(mat_T)
