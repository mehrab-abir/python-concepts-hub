nRows = int(input("Number of rows: "))
nCols = int(input("Number of columns: "))

for row in range(nRows):
    for col in range(nCols):
        if row == 0 or row == nRows - 1 or col == 0 or col == nCols-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        

# * * * * * * * *     
# *             *     
# *             *     
# *             *     
# * * * * * * * *     
