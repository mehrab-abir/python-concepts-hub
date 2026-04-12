# nums = input("Enter numbers: ")  #output: 2 3 4 5 6
# nums = input("Enter numbers: ").split() #output: ['2', '3', '4', '5', '6'] 

#map through all items, make them integer and store them in a list
nums = list(map(int, input("Enter numbers: ").split()))

print(nums) ## output -> [6, 3, 2, 1]

""" print("Numbers : ")
for num in nums:
    print(num) """
    
    ##using index
""" for i in range(len(nums)):
    print(f"{nums[i]} and type: {type(nums[i])}") """