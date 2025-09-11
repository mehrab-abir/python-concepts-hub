#function()

# def greet():
#     print("Hello Friend!\nWhat's your name?")
#     name = input()
#     print(f"I'm Batman. Nice to meet you {name}")

# print("Some other stuffs")

# greet()

def product(num1,num2):
    result = num1 * num2
    return result

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))

result = product(num1,num2)
print(f"Product of {num1} and {num2}: {result}")