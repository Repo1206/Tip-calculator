#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill?\n$"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people_to_split=int(input("How many people will split the bill?\n"))
tip = tip_percentage / 100
bill_tip = total_bill * tip
total = bill_tip + total_bill
result = total / people_to_split
print(f"Each person should pay ${result:.2f}")