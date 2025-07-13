

curr = input("How old are you?")
while not curr.isdigit():
    curr = input("Please enter a valid number for your current age: ")
curr = int(curr)

print(f"In 2050, you will be {curr + 27} years old.")