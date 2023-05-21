lis = input("Insert numbers: ")
lis = lis.split()

new_lis = [float(number) for number in lis]

minimun = min(new_lis)
maximun = max(new_lis)

print(f"The minimun number is {minimun} and the maximun number is {maximun}")