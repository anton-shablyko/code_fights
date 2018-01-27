def commonCharacterCount(s1, s2):
    s1, s2 = list(s1), list(s2)
    counter = 0
    for i in s1:
        if i in s2:
            s2.remove(i)
            counter += 1
    return counter

s1 = "aabcc"
s2 = "adcaa"

commonCharacterCount(s1, s2)