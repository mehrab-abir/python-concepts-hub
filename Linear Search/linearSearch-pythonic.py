#Linear search in pythonic way- shortcut
nums = list(map(int, input("Enter numbers: ").split()))

""" print("The numbers: ")
for num in nums:
    print(num,end= " ")
print() #just a new line """


print("The numbers: "," ".join(map(str,nums)))

#search a number in the list
numberToSearch = int(input("Enter a number to search: "))

if numberToSearch in nums:
    index = nums.index(numberToSearch)
    print(f"{numberToSearch} found at index {index}")
else:
    print(f"{numberToSearch} not found in the list")