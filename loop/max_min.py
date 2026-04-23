## maximum number among 3 numbers

""" nums = list(map(int,input("Enter 3 numbers: ").split()))

num_1 = nums[0]
num_2 = nums[1]
num_3 = nums[2]

if((num_1 >= num_2) and (num_1 >= num_3)):
    print(f"Maximum is {num_1}")
elif((num_2 >= num_1) and (num_2 >= num_3)):
    print(f"Maximun is {num_2}")
else:
    print(f"Maximum is {num_3}")
     """
    
# print digits from right to left

t = int(input("Number of test cases: "))

for i in range(t):
    num = int(input("Enter a number: "))
    
    if(num == 0):
        print(num)
    else:
        while num != 0:
                digit = num % 10
                print(digit,end=" ")
                num = int(num / 10)
                # num //=10 # same as the line above
        print()
                