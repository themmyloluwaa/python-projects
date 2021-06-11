
one = int(input())
two = list(input())

print(two)


def matrix():
    mat = []

    for i in range(one):
        mat.append([])
        for ind in range(start, len(two)):
            if len(mat[i]) < one:
                mat[i].append(two[ind])
            else:
                start = ind
                break

    return mat


matrix_var = matrix()

longest = 0

for i in range(len(matrix_var)):
    for in range()
