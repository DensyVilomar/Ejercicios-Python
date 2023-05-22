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
    
minimun = min(lis)
maximun = max(lis)
    
print(f"The minimun number is {minimun} and the maximun nomber is {maximun}")    