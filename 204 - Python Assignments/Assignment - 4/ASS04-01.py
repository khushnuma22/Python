# Q.1. Write a Python program to create a file of numbers by taking input from the user and then
# display the content of the file. You can take input of non-zero numbers, with an appropriate
# prompt, from the user until the user enters a zero to create the file assuming that the numbers
# are non-zero.

while True :
    Num = int(input("Enter number or 0 for Exit : "))
    if Num == 0 :
        break
    else : 
        ASS04_01 = open("ASS04_01.txt", "a")
        String = str(Num)
        ASS04_01.write(String)
        ASS04_01.write("\n")
        ASS04_01.close()
        
ASS04_01 = open("ASS04_01.txt", "r")
print(ASS04_01.read())
ASS04_01.close()