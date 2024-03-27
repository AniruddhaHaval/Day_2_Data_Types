# 1st input: enter height in meters e.g: 1.65
height = float(input("enter height in meters: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("enter weight in kilograms: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / (height**2)

print("Your bmi is " + str(bmi))