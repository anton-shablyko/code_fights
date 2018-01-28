def avoidObstacles(inputArray):
    ia = sorted(inputArray)
    min_jump, max_jump = 2, max(ia)+2
    for i in range(min_jump, max_jump):
        x = [j for j in ia if j % i == 0]
        if len(x) == 0:
            return i


x = [5, 3, 6, 7, 9]
print(avoidObstacles(x))
