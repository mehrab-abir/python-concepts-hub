nums = list(map(int, input("Enter numbers: ").split()))

sortedNums = sorted(nums) #when a new list with the sorted numbers is required

print("The original list: "," ".join(map(str,nums)))
print("The sorted list: "," ".join(map(str,sortedNums)))