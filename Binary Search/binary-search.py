nums = list(map(int,input("Enter numbers: ").split()))

nums.sort()

print("The sorted numbers: "," ".join(map(str,nums)))

left = 0
right = len(nums)- 1

numberToSearch = int(input("Enter a number to search: "))
found = False
index = -1

while left <= right:
    mid = (left + right)//2

    if(nums[mid] == numberToSearch):
        found = True
        index = mid
        break
    elif(nums[mid] < numberToSearch):
        left = mid + 1
    else:
        right = mid - 1

if(found):
    print(f"{numberToSearch} found at index: {index}")
else:
    print(f"{numberToSearch} not found in the list")

