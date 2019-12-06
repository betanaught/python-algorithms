# Enter calculation: 5 * 6
# Return: 5 * 6 = 30

num1, operator, num2 = input('Enter Calculation: ').split()

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Error: incorrect operator entered")
