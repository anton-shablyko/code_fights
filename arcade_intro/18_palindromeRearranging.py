def palindromeRearranging(inputString):
    new_str = set(inputString)  # find a list of unique chard
    counter = 0
    if len(inputString) % 2 == 0:  # if number of chars is even check that each element is even
        for i in new_str:
            if inputString.count(i) % 2 != 0:
                return False
        return True

    elif len(inputString) % 2 > 0: # if number of chars is odd check that 1 or 0 uniques elements presented
        for i in new_str:
            if inputString.count(i) == 1:
                counter += 1
    if counter > 1:
       return False
    else:
      return True


print(palindromeRearranging('abcba'))