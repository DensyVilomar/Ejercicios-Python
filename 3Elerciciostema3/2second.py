try:
    grade = float(input("Insert your grade in range of 0.0 and 1.0: "))
except:
    print("Error, insert a number.")
    quit()
    
if grade < 0.0 or grade > 1.0:
    print("Error, insert a number in range of 0.0 and 1.0")
elif grade == 1.0:
    print("Excelent")
elif grade >= 0.9:
    print("Very good")
elif grade >= 0.8:
    print("Good")
elif grade >= 0.7:
    print("Ok")
elif grade >= 0.6:
    print("Enough")
else:
    print("It is not enough")