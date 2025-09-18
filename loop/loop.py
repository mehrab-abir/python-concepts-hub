nums = [2,6,3,4,8,1]

""" for num in nums:
    print(num) """

print(f"Length of the list 'nums': {len(nums)}")

print("************")
#print in one line, seperated by comma
""" for num in range(0,10,1):
    print(num, end=", ") """

print("**********************")

""" nums = [str(i) for i in range(1,15,1)]
print(", ".join(nums)) """

print("**********************")

#to access the index. In this case, access values using index as well
for i in range(len(nums)):
    print(f"{i} -> {nums[i]}")


