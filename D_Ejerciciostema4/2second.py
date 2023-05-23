lis = input("Insert numbers: ")
lis = lis.split()

new_lis = [float(number) for number in lis]

minimum = min(new_lis)
maximum = max(new_lis)

print(f"The minimum number is {minimum} and the maximum number is {maximum}")