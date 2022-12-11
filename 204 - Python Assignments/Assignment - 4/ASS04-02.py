# Q.2. Write a Python program to create a text file of multiple lines. Display the following:
# 1. Entire text file
# 2. 1st n lines of the text tile.
# 3. m lines starting from the nth line
# 4. number of words in each line

while True :
    Data = input("Enter String or 0 for Exit : ")
    if Data == "0" :
        break
    else :
        ASS04_02 = open("ASS04_02.txt", "a")
        ASS04_02.write(Data + "\n")
        ASS04_02.close()

ASS04_02 = open("ASS04_02.txt", "r")
print("----------Print Entire file----------")
print(ASS04_02.read())
ASS04_02.close()

ASS04_02 = open("ASS04_02.txt", "r")
Data1 = int(input("Give number how many lines print from the start : "))
print("----------1st n lines of the file----------")
for i in range(Data1) :
    print(ASS04_02.readline().rstrip())

Data2 = int(input("\nGive number how many lines print from n'th line : "))
print("----------m lines starting from the n'th line----------")
Count = 0
for i in range(Data1, Data2):
    if Data2 <= Count or Data2 >= Data1 :
        print(ASS04_02.readline().rstrip())
    else:
        ASS04_02.readline()
        Count = Count + 1
ASS04_02.close()

ASS04_02 = open("ASS04_02.txt", "r")
Count = 1
print("\n----------Number of words in each line----------")
for i in ASS04_02 :
    Data3 = len(list(i.strip().split()))
    print(Count, ") Lines In Number Of Words :- ",Data3)
    Count += 1
ASS04_02.close()