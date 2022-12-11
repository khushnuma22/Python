# Q.2. Write a Python program to take input of positive numbers, with an appropriate prompt,
# from the user until the user enters a zero. Find total number of odd & even numbers entered
# and sum of odd and even numbers. Display total count of odd & even numbers and sum of
# odd & even numbers with appropriate titles.

SumEven = 0
SumOdd = 0
CntEven = 0
CntOdd = 0
while True:
    Num = int(input("Enter a number and 0 for exit : "))
    if Num < 0 :
        print("Enter Postive number.")
    elif Num == 0:
        break
    elif Num % 2 == 0:
        CntEven = CntEven + 1
        SumEven = SumEven + Num
    else:
        CntOdd = CntOdd + 1
        SumOdd = SumOdd + Num        
print("")
print("Count the Odd number is = ", CntOdd)
print("Count the Even number is = ", CntEven)
print("Count the Sum of Odd number is = ", SumOdd)
print("Count the Sum of Even number is = ", SumEven)