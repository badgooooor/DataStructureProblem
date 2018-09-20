def calCompound(start, interest, year):
    if year == 0:
        return start
    else:
        i = start * (interest/100)
        return calCompound(start+i, interest, year-1)


print(calCompound(10000, 0.5, 5))