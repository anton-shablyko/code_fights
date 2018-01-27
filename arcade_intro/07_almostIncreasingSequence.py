def check_pairs(seq):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            return i
    return -1


def almostIncreasingSequence(sequence):
    j = check_pairs(sequence)
    if j == -1:
        return True
    if check_pairs(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if check_pairs(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False

"""Good Solution but slow with large sets"""
# def almostIncreasingSequence(sequence):
#     if len(sequence) <= 2:
#         return True
#     x = (sequence[:i] + sequence[i + 1:] for i in range(len(sequence)))
#     for i in x:
#         if is_increasing(i):
#             return True
#         else:
#             continue
#     return False
#
# def is_increasing(seq):
#     if seq == sorted(seq):
#         if len(seq) == len(set(seq)):
#             return True
#     return False