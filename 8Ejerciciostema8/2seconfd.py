counter = 0
with open("zz.txt", "r") as file:
    for lines in file:
        if lines.startswith("From "):
            counter += 1
            lines = lines.split()
            email = lines[1]
            print(email)
            
print(f"There are {counter} lines that star with From")