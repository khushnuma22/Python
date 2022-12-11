# Q.4. Write a Python program to create a list of elements of any data type (mixed data type, i.e. some
# elements maybe of type int, some elements of type float and some elements of type string). Split
# this list into three tuples containing elements of same data type (i.e. 1st tuple of integers only,
# 2nd tuple of float only and 3rd tuple of strings only). Take input from the user to create the list.
# Sample Input: [25, 4.5, ‘Hello’, 90, 20, 7.5, 9.25, ‘World’]
# Output:
# List of Integers: [25, 90, 20]
# List of Float Values: [4.5, 7.5, 9.25]
# List of Strings: [‘Hello’, ‘World’]

My_List = []
Int_List = []
String_List = []
Float_List = []
while True :
    Data = input("Enter a Value and 0 for Exit : ")    
    if (Data == '0') :
        break
    else :
        if Data.isdigit() :
            My_List.append(int(Data))
        elif '.' in Data :
            try :
                My_List.append(float(Data))
            except :
                My_List.append(Data)
        else :
            My_List.append(Data)
for i in My_List :
    if isinstance(i, int) :
        Int_List.append(i)
    elif isinstance(i, float) :
        Float_List.append(i)
    else :
        String_List.append(i)
print(My_List)
print(Int_List)
print(String_List)
print(Float_List)