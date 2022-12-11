# Q.3. Write a Python program to take input of a positive number, with an appropriate prompt,
# from the user. The user should be prompted again to enter the number until the user enters
# a positive number. Check whether the number is a prime number or not and accordingly
# display appropriate message.

while True:
    Num = int(input("Enter a Number and 0 for Exit : "))
    if Num < 0 :
        print("Enter Postive Number.")
    elif Num == 0 : 
        break
    else:
        Prime = False
        for i in range(2 , Num):
            if(Num % i == 0):
                Prime = True
        if Prime == True:
            print("The Number is Prime")
        else:
            print("The Number is not Prime")