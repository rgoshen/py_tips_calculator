#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = (tip / 100) + 1

owed_per_person = (total_bill / people) * tip_percent

print(f"Each person should pay: ${round(owed_per_person, 2)}")