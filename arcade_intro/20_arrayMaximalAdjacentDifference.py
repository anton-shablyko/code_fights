def arrayMaximalAdjacentDifference(inputArray):
    result = 0
    for i in range(len(inputArray)-1):
        diff = abs(inputArray[i] - inputArray[i+1])
        if diff > result:
            result = diff
    return result
