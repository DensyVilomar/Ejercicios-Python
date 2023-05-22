lis = []
while True:
    numbers = input("Insert a number: ")
    if numbers == "q": break
    
    try:
        to_float = float(numbers)
    except:
        print("Insert a number, please.")
        continue
    
    lis.append(to_float)
    
minimum = min(lis)
maximum = max(lis)
    
print(f"The minimum number is {minimum} and the maximum number is {maximum}")    