import string

my_dict = {}
lis = []

request = input("Name of the file: ")

try:
    with open(request,"r") as file:
        for lines in file:
            lines = lines.translate(str.maketrans('', '', string.punctuation))
            lines = lines.lower()
            lines = lines.split()
            for words in lines:
                for letters in words:
                    if letters not in my_dict:
                        my_dict[letters] = 1
                    else:
                        my_dict[letters] += 1
except:
    print("Error, nonexistent file.")

for letter,amount in list(my_dict.items()):
    lis.append((letter,amount))

lis.sort()    

for letter,amount in lis:
    print(f"{letter}:{amount}")