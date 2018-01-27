def makeArrayConsecutive2(statues):
    optimal_range = [i for i in range(min(statues), max(statues)+1)]
    return len(optimal_range) - len(statues)


print(makeArrayConsecutive2([6, 2, 3, 8]))