def arrayChange(inputArray):
    counter = 0
    for i in range(len(inputArray)-1):
        s1, s2 = inputArray[i], inputArray[i+1]
        if s1 >= s2:
            d = (s1-s2+1)
            inputArray[i+1] += d
            counter += d
    return counter


print(arrayChange([-1000, 0, -2, 0]))


