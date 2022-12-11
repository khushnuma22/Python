# Q.7. Write a Python program to create a text file of multiple lines. Take input of a word from the
# user and then display all the lines from the file containing this word along with the frequency of
# the word in that line.

while True :
    ASS04_07 = open("ASS04_07.txt", "a")
    Data = input("Enter a String or 0 for Exit : ")
    if Data == '0' :
        break
    else :
        ASS04_07.write(Data + "\n")
    ASS04_07.close()

ASS04_07 = open("ASS04_07.txt", "r")
print(ASS04_07.read())
ASS04_07.close()

ASS04_07 = open("ASS04_07.txt", "r")
Word = input("Enter word you want to search : ")
c = 0

for i in ASS04_07:
    Count = 0
    for j in list(i.rstrip().split()):
        if Word == j:
            Count = Count + 1
            words = i
    c = c + 1
    if Count != 0:
        print(words ,"frequency is", Count, " the '", Word, "' in that line (", c,")")
ASS04_07.close()