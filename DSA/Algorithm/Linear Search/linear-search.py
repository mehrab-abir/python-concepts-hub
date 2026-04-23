nums = list(map(int, input("Enter numbers: ").split()))

print("The numbers: ")
for num in nums:
    print(num, end=" ")
print()

numberToSearch = int(input("Enter a number to search: "))

found = False
foundIndex = -1


for i in range(len(nums)):
    if(nums[i] == numberToSearch):
        found = True
        foundIndex = i
        break

if(found):
    print(f"{numberToSearch} found at index {foundIndex}")
else:
    print(f"{numberToSearch} not found in the list")



