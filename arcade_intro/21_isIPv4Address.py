def isIPv4Address(inputString):
    if inputString.count('.') == 3:
        lst = inputString.split('.')
        for i in lst:
            if i is '' or i.isdigit() is False:
                return False
            elif int(i) in range(0, 256):
                continue
            return False
        return True
    return False


x = "15.16.254.1"
print(isIPv4Address(x))