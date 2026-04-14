""" first = int(input("Enter first number: "))
second = int(input("Enter second number: ")) """

nums = input("Enter two numbers: ").split() # a list of strings

last_1 = int(nums[0]) % 10
last_2 = int(nums[1]) % 10

print(f"Result: {last_1 + last_2}")