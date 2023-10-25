list = [1, 5, 12, 44, 6, 3, 5, 0, 5]
dupList = []
length = len(list)

for i in range (length):
    if list[i] == list[i]:
        dupList.append (list[i])

print ("List of dupes: ", dupList)

