# First try:
# def adjacentElementsProduct(inputArray):
#     running_max = 0
#     for i in range(0, len(inputArray)-1):
#        arr = inputArray[i:i+2]
#        _max = arr[0] * arr[1]
#
#        if _max > running_max or running_max == 0:
#            running_max = _max
#     print(running_max)
#     return running_max

# One liner ))
def adjacentElementsProduct(inputArray):
    x = [inputArray[i]*inputArray[i+1] for i in inputArray]
    return max(x)

adjacentElementsProduct([-23, 4, -3, 8, -12])
