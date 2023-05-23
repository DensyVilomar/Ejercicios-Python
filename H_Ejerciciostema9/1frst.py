my_dict = {}
with open("zz.txt", "r") as file:
    for lines in file:
        if lines.startswith("From "):
            lines = lines.split()
            word = lines[2]
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1
                
print(my_dict)