Request = input("Insert a name of a file: ")
try:
    file = open(Request, "r")
except:
    print("Error, nonexistent file.")
    quit()
    
for lines in file:
    if lines.startswith("X-DSPAM-Confidence"):
        lines = lines.rstrip()
        search = lines.find(":")
        decimal = lines[search + 1:]
        to_float = float(decimal)
        print(decimal)

file.close()
