def addBorder(picture):
    result = []
    end = '*' * (len(picture[0])+2)
    result.append(end)
    for i in picture:
        result.append('*' + i + '*')
    result.append(end)
    return result

print(addBorder(['abc','def']))