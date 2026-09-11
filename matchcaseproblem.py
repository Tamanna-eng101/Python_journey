#Day of the Week 📅The Story: You want to make a digital calendar helper.
# Input: A number from 1 to 7.Your Task: Write a switch case where:1 prints "Saturday" (or Sunday, depending on your calendar!)7 prints "Friday"Any other number prints "Wrong day number!"

day_number = int(input("Enter  a day number (1-7) :"))

match day_number:
    case "1":
        print("Saturday")
    case "2":
        print("Sunday")
    case "3":
        print("Monday")
    case "4":
        print("Tuesday")
    case "5":
        print("Wednesday")
    case "6":
        print("Thursday")
    case "7":
        print("Friday")  
    case _:
        print("Wrong day number")

     