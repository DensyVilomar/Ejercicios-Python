counter = 0
Request = input("Insert a name of a file: ")
try:
    file = open(Request, "r")
except:
    print("Error, nonexistent file.")
    quit()
    
for lines in file:
    if lines.startswith("X-DSPAM-Confidence"):
        counter += 1
        lines = lines.rstrip()
        search = lines.find(":")
        decimal = float(lines[search + 1:])
        sum = decimal + decimal

        
file.close()

print(f"The average is {sum/counter}")