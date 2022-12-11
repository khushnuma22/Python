# Q.4. Write a Python program to create a file of elements of any data type (mixed data type, i.e. some
# elements maybe of type int, some elements of type float and some elements of type string). Split
# this file into three file containing elements of same data type (i.e. 1st file of integers only, 2nd
# file of float only and 3rd file of strings only). Take input from the user to create the file.

My_List = []
while True :
    Num = input("Enter value : ")
    if (Num == '0') :
        break
    else :
        if Num.isdigit() :
            My_List.append(int(Num))
        elif '.' in Num :
            try :
                My_List.append(float(Num))
            except :
                My_List.append(Num)
        else :
            My_List.append(Num)
        
ASS04_04 = open("ASS04_04.txt", "w")
for i in My_List :
    tmp = str(i)
    ASS04_04.write(tmp)
    ASS04_04.write("\n")
ASS04_04.close()

Int_List = []
String_List = []
Float_List = []
for i in My_List :
    if isinstance(i, int) :
        Int_List.append(i)
    elif isinstance(i, float) :
        Float_List.append(i)
    else :
        String_List.append(i)

ASS04_04_Int = open("ASS04_04_Int.txt", "w")
for i in Int_List :
    ASS04_04_Int.write(str(i) + "\n")
ASS04_04_Int.close()

ASS04_04_String = open("ASS04_04_String.txt", "w")
for i in String_List :
    ASS04_04_String.write(str(i) + "\n")
ASS04_04_String.close()

ASS04_04_Float = open("ASS04_04_Float.txt", "w")
for i in Float_List :
    ASS04_04_Float.write(str(i) + "\n")
ASS04_04_Float.close()

ass04 = open("ASS04_04.txt", "r")
print("\n----------All Values----------")
print(ass04.read())
ass04.close()

inttxt = open("ASS04_04_Int.txt", "r")
print("----------Int values----------")
print(inttxt.read())
inttxt.close()

strtxt = open("ASS04_04_String.txt", "r")
print("----------String values----------")
print(strtxt.read())
strtxt.close()

floattxt = open("ASS04_04_Float.txt", "r")
print("----------Float values----------")
print(floattxt.read())
floattxt.close()