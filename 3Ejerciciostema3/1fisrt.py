
try:
    hours = float(input("How many hours did you work?\n"))
    hourly_wage = float(input("What is your hourly wage?\n"))
except:
    print("Error, please insert a number.")
    quit()

if hours > 40:
    gross_salary = 40 * hourly_wage
    extra_hours = hours - 40
    new_hourly_salary = (1.5 * hourly_wage * extra_hours) 
    new_salary = new_hourly_salary + gross_salary
    print(new_salary) 
else:
    print(hours * hourly_wage)