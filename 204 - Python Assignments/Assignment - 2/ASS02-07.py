# Q.7. Consider a single list consisting of integer values, float values, character values, string
# values and lists. Write a Python program to do the following:
# 1) Count total number of elements in the list
# 2) Count total number of integer values, float values, character values, string
# values and lists Display all the values with appropriate titles.

My_List = [1, 2.3, 'Chirag', 'Khushi', 'Mini', 'p', [1, 2, 3], 2.8, 9]
Int_Count = 0
Float_Count = 0
Char_Count = 0
String_Count = 0
List_Count = 0
for i in My_List :
    if isinstance(i, int) :
        Int_Count += 1
    elif isinstance(i, float) :
        Float_Count += 1
    elif isinstance(i, list) :
        List_Count += 1
    elif isinstance(i, str) :
        if(len(i) == 1) :
            Char_Count += 1
        else :
            String_Count = String_Count + 1
print("TOtal Numbers of elements : ", len(My_List))
print("Number of Integers : ",Int_Count)
print("Number of  Float : ",Float_Count)
print("Number of  List : ",List_Count)
print("Number of  Characters : ", Char_Count)
print("Number of  String : ",String_Count)