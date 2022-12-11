# Q.4. Write a Python program to take input of a positive number, say N, with an appropriate
# prompt, from the user. The user should be prompted again to enter the number until the
# user enters a positive number. Find the sum of first N odd numbers and first N even
# numbers. Display both the sums with appropriate titles.

SumEven = 0
SumOdd = 0
CntEven = 0
CntOdd = 0
while True:
    N = int(input("Enter a Number and 0 for Exit : "))
    if N < 0 :
        print("Enter Postive Number")
    elif N == 0:
        break
    elif N % 2 == 0:
        CntEven = CntEven + 1
        SumEven = SumEven + N
    else:
        CntOdd = CntOdd + 1
        SumOdd = SumOdd + N
print("")
print(f"Count the Sum of {CntOdd} Odd Number is = {SumOdd}")
print(f"Count the Sum of {CntEven} Even Number is = {SumEven}")