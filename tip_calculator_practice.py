#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = float(input("What is total bill? "))
person = int(input("What is total no of persons? "))

tip_percentage = 1 + (float(input("What is tip percentage? "))) / 100
each_person_pay = ((total_bill / person)*tip_percentage)
each_person_pay = "{0:.3f}".format(each_person_pay)

# each_person_pay = round(each_person_pay,3)

print(f"Each person should pay {each_person_pay}")
