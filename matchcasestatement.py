# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: Less code, more readable, easier to maintain

from datetime import datetime

def days_of_week(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")

# Get the current day of the week (1 is Monday, 7 is Sunday)
current_day = datetime.now().isoweekday()
print(f"Today is day number {current_day}")
days_of_week(current_day)