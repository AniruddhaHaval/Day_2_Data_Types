print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = (int(input("What percentage tip would you like to give? 10, 12 or 15? ")))/100 + 1

# print(f"{tip_percentage}")

people = int(input("How many people to split the bill? "))

# share = round(((bill*tip_percentage)/people),2)
share = "{:.2f}".format((bill*tip_percentage)/people)
print(f"Each person should pay: ${share}")