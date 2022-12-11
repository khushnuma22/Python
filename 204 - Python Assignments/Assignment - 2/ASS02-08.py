# Q.8. Write a Python program to read a m X n matrix and find the following:
# 1) Find sum of each row and each column.
# 2) Find the highest and lowest from each row, each column, and the whole matrix.
# 3) Find the sum of its diagonal elements if the matrix is a square matrix.
# 4) Find the transpose of the matrix.
# Display all the values with appropriate titles.

M = int (input ("Enter the size of the Row : "))
N = int (input ("Enter the size of the Column : "))
a, Sum = [], 0
print ("\n-----Enter the co-efficients of the matrix-----")
for i in range (M):
    a.append([])
    for j in range (N):
        a[i].append(int (input ()))
        print (end="\n")

# for printing the matrix in appropirate sequence.................
for i in range(M):
    for j in range(N):
        print(a[i][j], end = " ")
    print()
    print (end="\n")

print ("\n-----the total sum of row and coulmn is -----")
print (end="\n")
# This statement will compute the
# sum of the matrix's rows elements
for i in range (M):
    for j in range (N):
        Sum = Sum + a[i][j]

    print ("The Sum of the ", i, " Position row is = ", Sum)
    Sum = 0
    print (end="\n")
    Sum = 0

# This statement will compute the
# sum of the matrix's columns elements
for j in range (M):
    for i in range (N):
        Sum = Sum + a[i][j]

print ("The Sum of the ", j, " position column is = ", Sum)
Sum = 0

#FOR diagonal sum of the MATRIX...........
print (end="\n")
print ("\n-----the digonal sum of the matrix is : -----")
print (end="\n")
L = len(a[0])
Sum=0
for i in range(M):
    Sum += a[i][L-i-1]

print("diagonal elements sum is :", Sum)

#FOR TRANSPOSE sum of the MATRIX...........
print (end="\n")
print ("\n-----the transpose of the matrix is : -----")
print (end="\n")
def transpose(a, b):
    for i in range(M):
        for j in range(N):
            b[i][j] = a[j][i]

b = a[:][:] # To store result
transpose(a, b)

print("transpose of the matrix is ")
for i in range(M):
    for j in range(N):
        print(b[i][j], " ", end='')
    print()