age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_in_int = int(age) * 52
life_in_weeks = 90 * 52

life_left_in_weeks = life_in_weeks - age_in_int

print(f"You have {life_left_in_weeks} weeks left")
