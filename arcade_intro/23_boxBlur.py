def boxBlur(image):
    result = []
    for h in range(len(image)-2):
        t_result = []
        for w in range(len(image[0])-2):
            top_row = image[h][w:w+3]
            mid_row = image[h+1][w:w+3]
            low_row = image[h+2][w:w+3]
            blur = (sum(top_row + mid_row + low_row))//9
            t_result.append(blur)
        result.append(t_result)
    return result


image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]
print(boxBlur(image))