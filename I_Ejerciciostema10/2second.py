my_dict = {}
lis = []

request = input("Name of the file: ")

try:
    with open("zz.txt","r") as file:
        for lines in file:
            if lines.startswith("From "):
                lines = lines.split()
                extraction = lines[5]
                division = extraction.split(":")
                hour = division[0]
                if hour not in my_dict:
                    my_dict[hour] = 1
                else:
                    my_dict[hour] += 1
except:
    print("Error, nonexistent file")  
              
for hour,amount in list(my_dict.items()):
    lis.append((amount,hour))
    
lis.sort(reverse=True)

for hour,amount in lis:
    print(hour,amount)            