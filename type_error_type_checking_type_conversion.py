num_char = len(input("What is your name? "))

# print("Your name has " + num_char + "characters.")
# TypeError: can only concatenate str (not "int") to str

print(type(num_char))
#<class 'int'>

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print(70 + float("100.5"))
# print(70 + 100.5)

print(str(70) + str(100))

