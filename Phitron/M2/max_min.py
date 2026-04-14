## maximum number among 3 numbers

nums = list(map(int,input("Enter 3 numbers: ").split()))

num_1 = nums[0]
num_2 = nums[1]
num_3 = nums[2]

if((num_1 >= num_2) and (num_1 >= num_3)):
    print(f"Maximum is {num_1}")
elif((num_2 >= num_1) and (num_2 >= num_3)):
    print(f"Maximun is {num_2}")
else:
    print(f"Maximum is {num_3}")
    
    
    
## min is same