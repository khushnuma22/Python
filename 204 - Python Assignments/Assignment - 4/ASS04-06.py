# Q.6. Write a Python program to create a file of strings by taking input from the user and then create
# a dictionary containing each string along with their frequencies. (e.g. if the file contains ‘apple’,
# ‘banana’, ‘fig’, ‘apple’, ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’ then the output should
# be {'apple': 3, 'banana': 2, 'fig': 3, 'grapes': 2}.

def Count_Freg(List) :
    Freg = {}
    for items in List :
        Freg[items] = List.count(items)     
    print(Freg)

while True :
    Data = input("Enter a string and 0 for Exit : ")
    if Data == "0" :
        break
    else :
        ASS04_06 = open("ASS04_06.txt", "a")
        ASS04_06.write(Data + "\n")
        ASS04_06.close()

List = []
ASS04_06 = open("ASS04_06.txt", "r")
for i in ASS04_06 :
    current_place = i[:-1]
    List.append(current_place)

print(List, "\n")
Count_Freg(List)
ASS04_06.close()