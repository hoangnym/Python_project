#### Create a tip calculator

### Ask for total bill
total = float(input("What was the total bill?\n"))

### How many people attended the event
people = int(input("How many people to split the bill?\n"))

#### WHat percentage tip would you like to give? 10, 12, or 15?
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))/100

### Output
result = round((total * (1+tip)) / people, 2)

print(f"The total bill is {total}, the tip is {round(total * tip, 2)} which means that each person pays {result}.")