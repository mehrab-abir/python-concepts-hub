nRows = int(input("Number of rows: "))
nCols = int(input("Number of columns: "))

matrixA = []
matrixB = []
matA_x_matB = []

print("Input for matrix A: ");
for i in range(nRows):
    row = list(map(int,input(f"Enter {nCols} numbers for row {i+1}: ").split()))
    matrixA.append(row)
   
print()
 
print("Input for matrix B: ");
for i in range(nRows):
    row = list(map(int,input(f"Enter {nCols} numbers for row {i+1}: ").split()))
    matrixB.append(row)

# multiplication
# for square matrix
# for non-square matrix, logic has to be adjusted accordingly
for row in range(nRows):
    new_row = []
    for i in range(nCols):
        sum = 0;
        for col in range(nCols):
            sum = sum + matrixA[row][col] * matrixB[col][i]
        new_row.append(sum)
    matA_x_matB.append(new_row)


for row in matA_x_matB:
    for cell in row:
        print(cell, end=" ")
    print()