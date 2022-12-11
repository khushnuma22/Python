# Q.3. Write a Python program to create a file of numbers by taking input from the user. Split this file
# into two files where one file contains odd numbers, and the other file contains even numbers
# from the file. You can take input of non-zero numbers, with an appropriate prompt, from the
# user until the user enters a zero to create the file assuming that the numbers are non-zero.

Odd = open("ASS04_03_Odd.txt", "w")
Even = open("ASS04_03_Even.txt", "w")

while True :
    Num = int(input("Enter Number or 0 for Exit : "))
    if Num == 0 :
        break
    else :
        if Num % 2 == 0 :
            Even.write(str(Num) + "\n")
        else :
            Odd.write(str(Num) + "\n")
Odd.close()
Even.close()

Odd = open("ASS04_03_Odd.txt", "r")
print("----------Odd Numbers----------")
print(Odd.read())
Odd.close()

Even = open("ASS04_03_Even.txt", "r")
print("----------Even Numbers----------")
print(Even.read())
Even.close()