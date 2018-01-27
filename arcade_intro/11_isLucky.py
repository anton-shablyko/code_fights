
def isLucky(n):
    n = [int(i) for i in str(n)]  # convert int to list
    d = len(n)//2  # find a divider index
    a, b = n[:d], n[d:]  # split list in half
    return sum(a) == sum(b)  # compare

isLucky(1230)