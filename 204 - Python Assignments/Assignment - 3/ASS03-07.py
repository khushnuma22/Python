# Q.7. Write a Python program to create a list of strings by taking input from the user and then create
# a dictionary containing each string along with their frequencies. (e.g. if the list is [‘apple’,
# ‘banana’, ‘fig’, ‘apple’, ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’] then output should be
# {'apple': 3, 'banana': 2, 'fig': 3, 'grapes': 2}.

def Count_Frequency(list) :
    freg = {}
    for items in list :
        freg[items] = list.count(items)     
    print(freg)

My_List = []
while True :
    Data = input("Enter a string and 0 for Exit : ")
    if Data == "0" :
        break
    else :
        My_List.append(Data)
Count_Frequency(My_List)