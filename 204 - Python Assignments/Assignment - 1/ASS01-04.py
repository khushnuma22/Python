First = int(input("Enter First Number : "))
Second = int(input("Enter Second Number : "))
Third = int(input("Enter Third Number : "))
print("First number is : ", First)
print("Second number is : ", Second)
print("Third number is : ", Third)
if First > Second and First > Third :
    Largest = First
elif Second > Third:
    largest = Second
else:
    Largest = Third
print(Largest, "is a Largest number !")