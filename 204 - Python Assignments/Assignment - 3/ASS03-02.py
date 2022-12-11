# Q.2. Write a Python program to create a list of lists of numbers (i.e. each element of the list is a list
# of numbers e.g. [[1, 2], [3, 2, 5], [1], [5, 3, 6, 7]]. Then generate a list from the given list where
# each element of the list is the length of each list in the given list. i.e. for the given example the
# output should be [2, 3, 1, 4]. You can take input of non-zero numbers, with an appropriate
# prompt, from the user until the user enters a zero to create the list assuming that the numbers
# are non-zero.
# Sample Input: [[1, 2], [3, 2, 5], [1], [5, 3, 6, 7]]
# Output: [2, 3, 1, 4]

Final_List = []
Answer = []
while True :
    List_Size = int(input("Enter the Number of Sub_List : "))
    if List_Size == 0 :
        break
    else :
        Sub_List = []
        for i in range(List_Size) :
            Num = int(input("Enter Single Number and Press Enter : "))
            Sub_List.append(Num)
        Final_List.append(Sub_List)
        print("\n")
        
for listelement in Final_List :
    Count = len(listelement)
    Answer.append(Count)

print("list is ", Final_List)
print(Answer)