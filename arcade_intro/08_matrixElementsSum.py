def matrixElementsSum(matrix):
    n = [i for i in matrix]
    for i in matrix:
        for j, z in enumerate(i):
            if z == 0:
                nm = [i[j] = 0 for i in matrix]
                print(nm)
            print(j, z)

    print(n)


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrixElementsSum(matrix)