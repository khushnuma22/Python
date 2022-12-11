# Q.8. Write a Python program to input a string that is a list of words separated by commas. Construct
# a dictionary that contains all these words as keys and their frequencies as values. Then display
# the words with their quantities.

Input_List = []
Output_List = {}
while True :     #Taking input from user
    Data = input("Enter a String or 0 for Exit : ")
    if Data == '0' :
        break
    else :
        Input_List.append(Data)
x = len(Input_List)
for i in range(x) :
    Output_List[Input_List[i]] = len(Input_List[i])
print("List : ", Input_List)
print("Output : ", Output_List)