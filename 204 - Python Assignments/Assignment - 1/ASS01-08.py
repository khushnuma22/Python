First = input("Enter First Number : ")
Second = input("Enter Second Number : ")
Third = input("Enter Third Number : ")
Temp = False

if First.strip().isdigit():
    print("First number is : ", First)
else:
    Temp = True
    print("First input is a String")
    
if Second.strip().isdigit():
    print("Second number is : ", Second)
else:
    Temp = True
    print("Second input is a String")
    
if Third.strip().isdigit():
    print("Third number is : ", Third)
else:
    Temp = True
    print("Third input is a String")
    
if Temp == True:
    print("Somthing is wrong !")
else :
    if First > Second and First > Third :
        Largest = First
    elif Second > Third:
        largest = Second
    else:
        Largest = Third
print(Largest, "is a Largest number !")