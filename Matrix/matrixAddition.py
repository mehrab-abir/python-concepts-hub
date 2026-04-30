nRows = int(input("Number of rows: "))
nCols = int(input("Number of columns: "))

matrixA = []
matrixB = []
matA_plus_matB = []

print("Input for matrix A: ");
for i in range(nRows):
    row = list(map(int,input(f"Enter {nCols} numbers for row {i+1}: ").split()))
    matrixA.append(row)
   
print()
 
print("Input for matrix B: ");
for i in range(nRows):
    row = list(map(int,input(f"Enter {nCols} numbers for row {i+1}: ").split()))
    matrixB.append(row)

for row in range(nRows):
    new_row = []
    for col in range(nCols):
        sum = matrixA[row][col] + matrixB[row][col]
        new_row.append(sum)
    matA_plus_matB.append(new_row)

for row in matA_plus_matB:
    for cell in row:
        print(cell, end=" ")
    print()