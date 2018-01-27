# TASK: https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def allLongestStrings(inputArray):
    longest = max(inputArray, key=len) # find the longest string in the list
    result = [i for i in inputArray if len(i) == len(longest)]
    return result

inputArray=["aba", "aa", "ad", "vcd", "aba"]

allLongestStrings(inputArray)