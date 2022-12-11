# Q.9. Write a Python program to read 2 matrices and find the following, if it is possible to do so:
# 1) Find sum of both the matrices.
# 2) Find difference of both the matrices.
# 3) Find product of both the matrices.
# Display all the values with appropriate titles.


print("---------------ENTER THE FIRST MATRIX--------------------")
X = int (input ("Enter the size of the Row : "))
Y = int (input ("Enter the size of the Column : "))
a, Sum = [], 0
print ("\n-----Enter the co-efficients of the matrix-----")
for i in range (X):
    a.append([])
    for j in range (Y):
        a[i].append(int (input ()))
        print (end="\n")

# for printing the matrix in appropirate sequence.................
for i in range(X):
    for j in range(Y):
        print(a[i][j], end = " ")
    print()
print (end="\n")

print("---------------- ENTER THE SECOND MATRIX--------------------")
M = int (input ("Enter the size of the Row : "))
N = int (input ("Enter the size of the Column : "))
b, Add = [], 0
print ("\n-----Enter the co-efficients of the matrix-----")
for i in range (M):
    b.append([])
    for j in range (N):
        b[i].append(int (input ()))
    print (end="\n")

# for printing the matrix in appropirate sequence.................
for i in range(M):
    for j in range(N):
        print(b[i][j], end = " ")
    print()
print (end="\n")

#Find sum of both the matrices
print ("\n-----the sum of both the matrices -----")
print (end="\n")
result = [[a[i][j] + b[i][j]
for j in range(len(a[0]))]
for i in range(len(a))]
for r in result:
    print(r)

#Find difference of both the matrices.
print("\n-----the diffrence of both the matrices -----")
print (end="\n")
result = [[a[i][j] - b[i][j]
for j in range(len(a[0]))]
for i in range(len(a))]
for r in result:
    print(r)
#Find prodcut of both the matrices.
print ("\n-----the product of both the matrices -----")
print (end="\n")
for i in range(len(a)):
 # iterating by column by B
    for j in range(len(b[0])):
# iterating by rows of B
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for r in result:
    print(r)