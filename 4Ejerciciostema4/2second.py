def calculator_grade(grade):
    
    try:
        grade = float(grade)
    except:
        return("Error, insert a number.")
    
    if grade < 0.0 or grade > 1.0:
        return("Error, insert a number in range of 0.0 and 1.0")
    elif grade == 1.0:
        return("Excelent")
    elif grade >= 0.9:
        return("Very good")
    elif grade >= 0.8:
        return("Good")
    elif grade >= 0.7:
        return("Ok")
    elif grade >= 0.6:
        return("Enough")
    else:
        return("It is not enough")
    
print(calculator_grade(0.99))