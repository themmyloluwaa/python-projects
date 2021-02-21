
def print_calculation(compute):
    print("The result of your computation is", str(compute))


print('What is your name')

name = input()

print("Welcome", name)
print('Chose an operation below and input your numbers')

operations = ["+", "-", "*", "/", "**", "%"]

isOperandSelected = False

selectedOperand = None

print('Please select an operation below')
for i in range(len(operations)):
    print("Press " + str(i) + " and hit enter to " + operations[i])

while not isOperandSelected:
    selectedOperand = int(input())
    if(selectedOperand < 0 or selectedOperand > len(operations) or selectedOperand == None):
        print('You selected an operation beyond the scope of available operations, please try again')
    else:
        print('You have selected ' + str(selectedOperand))
        isOperandSelected = True
print()

print('Your first number')
num1 = int(input())

print('Your second number')
num2 = int(input())

print('Performing magic with the numbers you inputed.')
print()
print('Any moment from now...')
print()
if(selectedOperand == 0):
    print('You selected an addition operation')
    print_calculation(num1 + num2)
elif selectedOperand == 1:
    print("You selected a subtraction operation")
    print_calculation(num1 - num2)
elif selectedOperand == 2:
    print("You selected a multiplication operation")
    print_calculation(num1 * num2)
elif selectedOperand == 3:
    print("You selected a division operation")
    print_calculation(num1 // num2)
elif selectedOperand == 4:
    print("You selected a power operation")
    print_calculation(num1 ** num2)
elif selectedOperand == 5:
    print("You selected a reminder/modulo operation")
    print_calculation(num1 % num2)

print()
print("All done")
