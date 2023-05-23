my_dict = {}
with open("zz.txt", "r") as file:
    for lines in file:
        if lines.startswith("From "):
            lines = lines.split()
            email = lines[1]
            if email not in my_dict:
                my_dict[email] = 1
            else:
                my_dict[email] += 1

print(my_dict)