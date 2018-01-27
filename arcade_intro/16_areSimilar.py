def areSimilar(a, b):
    if a == b:  # check if sets are identical
        return True

    if sorted(a) != sorted(b):  # check if set of elements in each set is the same
        return False

    new_r = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            new_r += 1

    return True if new_r in (0, 2) else False



a = [2, 2, 1]
b = [2, 1, 1]
print(areSimilar(a, b))