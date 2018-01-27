def sortByHeight(a):
    a0 = sorted([i for i in a if i != -1])
    result = []
    for i in a:
        if i == -1:
            result.append(i)
        else:
            result.append(a0.pop(0))
    return result


sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])