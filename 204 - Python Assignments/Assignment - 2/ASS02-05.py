# Q.5. Consider a list of numbers. Write a Python program to do the following:
# 1) Count total number of numbers in the list
# 2) Sum and Average of all the numbers in the list
# 3) Count and sum of all the odd numbers in the list
# 4) Count and sum of all the even numbers in the list
# 5) Find the largest number in the list
# 6) Find the smallest number in the list
# Display all the values with appropriate titles.

SumEven = 0
SumOdd = 0
CntEven = 0
CntOdd = 0
Total = 0
Sum = 0
List1 = []
while True :
    Num = int(input("Enter a Number and 0 for Exit : "))
    if Num < 0 :
        print("Enter Postive Number.")
    elif Num == 0:
        break
    elif Num % 2 == 0:
        CntEven = CntEven + 1
        SumEven = SumEven + Num
    else:
        CntOdd = CntOdd + 1
        SumOdd = SumOdd + Num
    Total = CntOdd + CntEven
    Sum = SumOdd + SumEven
    Average = Sum/Total
    List1.append(Num)
print("")
print(f"1. The Total number is = {Total}")
print(f"2. The Avegrage is {Average} and Sum is {Sum}")
print(f"3. The Total Odd number is {CntOdd} and Sum is {SumOdd}")
print(f"4. The total Even number is {CntEven} and Sum is {SumEven}")
print(f"5. Largest element is : {max(List1)}")
print(f"6. Smallest element is : {min(List1)}")