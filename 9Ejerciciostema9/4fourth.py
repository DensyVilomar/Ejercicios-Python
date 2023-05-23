my_dict = {}
with open("zz.txt","r") as file:
    for lines in file:
        if lines.startswith("From "):
            lines = lines.split()
            email = lines[1]
            division = email.find("@")
            domian = email[division + 1:]
            if domian not in my_dict:
                my_dict[domian] = 1
            else:
                my_dict[domian] += 1
                
print(my_dict)