def almostIncreasingSequence(sequence):
    if len(sequence) <= 2:
        return True
    # generate a list of sequences without one number
    # [1,2,3] ==> [[2, 3], [1, 3], [2, 3]]
    x = (sequence[:i] + sequence[i + 1:] for i in range(len(sequence)))
    for i in x:
        if is_increasing(i):
            return True
        else:
            continue
    return False

def is_increasing(seq):
    if seq == sorted(seq):
        if len(seq) == len(set(seq)):
            return True
    return False



print('\nThese should be True.')
print(almostIncreasingSequence([]))
print(almostIncreasingSequence([1]))
print(almostIncreasingSequence([1, 2]))
print(almostIncreasingSequence([1, 2, 3]))
print(almostIncreasingSequence([1, 3, 2]))
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))
print(almostIncreasingSequence([0, -2, 5, 6]))
print(almostIncreasingSequence([1, 1]))
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
print(almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]))
print(almostIncreasingSequence([1, 2, 2, 3]))

print('\nThese should be False.')
print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([3, 2, 1]))
print(almostIncreasingSequence([1, 1, 1]))
print(almostIncreasingSequence([1, 1, 1, 2, 3]))