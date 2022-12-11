# Q.3. Write a Python program to create a list of numbers by taking input from the user. Split this list
# into two tuples where one tuple contains odd numbers, and the other tuple contains even
# numbers from the list. You can take input of non-zero numbers, with an appropriate prompt,
# from the user until the user enters a zero to create the list assuming that the numbers are nonzero.
# Sample Input: [10, 12, 13, 90, 43, 32, 30, 11]
# Output:
# Tuple of Odd Numbers: (13, 43, 11)
# Tuple of Even Numbers: (10, 12, 90, 32, 30)

My_List = []
while True :
    Num = int(input("Enter a Number and 0 for Exit : "))
    if(Num == 0) :
        break
    else :
        My_List.append(Num)
Odd = []
Even = []
for i in My_List :
    if(i % 2 == 0) :
        Even.append(i)
    else :
        Odd.append(i)
Odd_Tuple = tuple(Odd)
Even_Tuple = tuple(Even)
print(My_List)
print(Odd_Tuple)
print(Even_Tuple)