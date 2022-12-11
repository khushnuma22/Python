# Q.1. Write a Python program to create a list of numbers by taking input from the user and then remove
# the duplicates from the list. You can take input of non-zero numbers, with an appropriate
# prompt, from the user until the user enters a zero to create the list assuming that the numbers
# are non-zero.
# Sample Input: [10, 34, 18, 10, 12, 34, 18, 20, 25, 20]
# Output: [10, 34, 18, 12, 20, 25]

List = []
while True :
    Num = int(input("Enter a Number and 0 for Exit : "))
    if(Num == 0) :
        break
    else :
        List.append(Num)

def Remove(List) :
    New_List = []
    for num in List :
        if num not in New_List :
            New_List.append(num)
    return New_List

Final_List = Remove(List)
print("Original List", List)
print("List after Remove Duplicate Items", Final_List)