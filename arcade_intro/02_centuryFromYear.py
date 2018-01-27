def centuryFromYear(year):
    return year // 100 if year % 100 == 0 else (year // 100) + 1

    # if year%100 == 0:
    #     return year//100
    # else:
    #     return (year//100) + 1
