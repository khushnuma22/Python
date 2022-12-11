# Q.1. Write a Python program to take input of non-zero numbers, with an appropriate prompt,
# from the user until the user enters a zero. Find total number of numbers entered and their
# sum. Display count and sum with appropriate titles.

Sum = 0
Total = 0
while True:
    Num = int(input("Enter a Number or 0 for exit : "))
    if Num < 0 :
        print("Enter Positive number.")
    elif Num == 0:
        break
    else:
        Sum += Num
    Total = Total + 1
print("")
print("The total of the Sum is ", Sum)
print("The total Number is ", Total)