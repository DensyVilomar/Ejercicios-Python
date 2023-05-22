lis = []
with open("zzz.txt", "r") as file:
    for lines in file:
        lines = lines.split()
        for word in lines:
            if word not in lis:
                lis.append(word)
print(lis)                              