nRowsA = int(input("Number of rows for matrix A: "))
nColsA = int(input("Number of columns for matrix A: "))

print(f"For matrix multiplication, number of rows of matrix B must be equal to the number of columns of matrix A.\nTherefor, number of rows of matrix B = {nColsA}")

nRowsB = nColsA;
nColsB = int(input("Number of columns for matrix B: "))

matrixA = []
matrixB = []
matA_x_matB = []

print("Input for matrix A: ");
for i in range(nRowsA):
    row = list(map(int,input(f"Enter {nColsA} numbers for row {i+1} of matrix A: ").split()))
    matrixA.append(row)
   
print()
 
print("Input for matrix B: ");
for i in range(nRowsB):
    row = list(map(int,input(f"Enter {nColsB} numbers for row {i+1} of matrix B: ").split()))
    matrixB.append(row)

# multiplication
for row in range(nRowsA):
    new_row = []
    for i in range(nColsB):
        sum = 0;
        for col in range(nRowsB):
            sum = sum + matrixA[row][col] * matrixB[col][i]
        new_row.append(sum)
    matA_x_matB.append(new_row)


for row in matA_x_matB:
    for cell in row:
        print(cell, end=" ")
    print()
