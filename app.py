# This function adds two numbers
def add(x, y):
    return x + y

# This function substracts two numbers
def substract(x, y):
    return x - y

# This function multiplication two numbers
def multiply(x, y):
    return x * y

# This function Divides two numbers
def divide(x, y):
    return x / y

print("Select Operation.")
print('1. Add')
print("2. Subtract")
print('3. Multiply')
print('4.Divide')


while True:
    # Take input from user 
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        # Exception handle the Invalid value enter
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', substract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        else:
            print(num1, '/', num2, '=', divide(num1, num2))
        
        # check if user want another calculation
        # Break the while loop if answer is no 
        if input("Let's do next calculaton? (yes/no): ") == 'no': 
            print("You exited the program.")
            break
    else:
        print("Invalid Input")
