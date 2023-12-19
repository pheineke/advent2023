test = open("day1test.txt", mode="r")



lines = test.readlines()
linenumber = len(lines)
#print(lines)


for j in lines:
    numbers = []
    for x in range(len(j)):
        jx = j[x]
        try:
            jx = int(jx)
            #print(jx)
            numbers.append(jx)
        except:
            pass
    print(f"{numbers[0]}{numbers[len(numbers)-1]}")