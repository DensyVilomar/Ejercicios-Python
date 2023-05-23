def calculator_salary(hours,hourly_wage):
    
    try:
        hours = float(hours)
        hourly_wage = float(hourly_wage)
    except:
        return("Error, insert numbers.")

    if hours > 40:
        gross_salary = 40 * hourly_wage
        extra_hours = hours - 40
        new_hourly_salary = (1.5 * hourly_wage * extra_hours) 
        new_salary = new_hourly_salary + gross_salary
        return(new_salary) 
    else:
        return(hours * hourly_wage)
    
print(calculator_salary(45,10))