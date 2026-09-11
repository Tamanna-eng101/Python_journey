#Input: A character or string representing the light color: 'R' (Red), 'Y' (Yellow), 'G' (Green).
# Your Task: Create a switch case that prints:'R' → "Stop!"'Y' → "Slow Down!"'G' → "Go!"
#Any other letter → "Invalid Signal!"

light_color = "_"
match light_color:

    case "R":
        print("Stop")
    case "Y":
        print("Slow down")
    case "G":
        print("Go")
    case    _:
         print("Invalid Signal")