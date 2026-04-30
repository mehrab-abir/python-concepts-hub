nRows = int(input("Number of rows: "));
nCols = int(input("Number of columns: "));

matrix = [];

for i in range(nRows):
    row = list(map(int,input(f"Enter {nCols} numbers for row {i+1}: ").split()))
    matrix.append(row)

# print(matrix)

for row in matrix:
    for cell in row:
        print(cell,end=" ")
    print()