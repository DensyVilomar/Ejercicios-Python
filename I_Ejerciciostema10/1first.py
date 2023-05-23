my_dict = {}
name_email = None
max_massages = None
lis = []
request = input("Name of the file: ")

try:
    with open(request,"r") as file:
        for lines in file:
            if lines.startswith("From "):
                lines = lines.split()
                email = lines[1]
                if email not in my_dict:
                    my_dict[email] = 1
                else:
                    my_dict[email] += 1
except:
    print("Error, file nonexistent")

for direction,amount in my_dict.items():
    if max_massages is None or amount > max_massages:
        name_email = direction
        max_massages = amount
        
for keys,values in list(my_dict.items()):
    lis.append((values,keys))
    
lis.sort(reverse=True)
    
for keys,values in lis:    
    print(keys,values)
    
print(f"The person who has more messages is {name_email} with {max_massages}")
       