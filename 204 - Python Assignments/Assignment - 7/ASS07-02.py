# Q.2. Write a Python program to create two text files containing different words. Create a list
# containing words that exist in both the files.

List = []
List1 = []
List2 = []
First_List = []
Second_List = []

ASS07_02_First = open("ASS07_02_First.txt", "r")
print("---------- First File ----------")
First_List =ASS07_02_First.read()
for data in list(First_List.rstrip().split()) :
        List1.append(data)
print(List1)
ASS07_02_First.close()

ASS07_02_Second = open("ASS07_02_Second.txt", "r")
print("---------- Second File ----------")
Second_List = ASS07_02_Second.read()
for data in list(Second_List.rstrip().split()) :
        List2.append(data)
print(List2)
ASS07_02_Second.close()
list.extend(List1, List2)
print(List)