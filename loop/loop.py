nums = [2,6,3,4,8,1]

for num in nums:
    print(num)

print(f"Length of the list 'nums': {len(nums)}")

print("************")
#print in one line, seperated by comma
for num in range(0,10,1):
    print(num, end=", ")

print("**********************")

nums = [str(i) for i in range(1,15,1)]
print(", ".join(nums))


