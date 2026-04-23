nums = list(map(int, input("Enter the numbers: ").split()))

print("The numbers: "," ".join(map(str,nums)))

#sort the numbers for binary search
nums.sort() #the original 'nums' list has been sorted

print("The numbers after being sorted: "," ".join(map(str,nums)))