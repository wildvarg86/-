def get_matrix(n, m,  value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i] = [value]* m
    return matrix

result = get_matrix(4, 3, 3)
print(result)
