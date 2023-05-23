counter = 0 
total = 0 

while True:
    numbers = input("Insert number and Q to leave: ").lower()    
    if numbers == "q": break
    try:
        string_to_float = float(numbers)
    except:
        print("Error, insert a number.")
        continue
    
    total += string_to_float
    counter += 1
    
print(f"You inserted {counter} numbers and their average is {total / counter}") 