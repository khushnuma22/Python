# Q.1. Write a Python program to create a text file of multiple lines. Display the following:
# 1. Line number and number of words in each line.
# 2. Display each line with the words in backward order.
# 3. Display line numbers of the empty lines.
# 4. Display all the lines that contain alphabets and digits both.
# 5. Display all the lines that contain only alphabets.

# ASS07_01 = open("ASS07_01.txt", "r")
# print("---------- First File ----------")
# # print(ASS07_01.read())
# list = ASS07_01.read()
# # print(list)
# ASS07_01.close()

ASS07_01 = open("ASS07_01.txt", "r")


Word_Count = 0
i = 0
str1 = ""

print("\n---------- Line number and number of words in each line. ----------")
for Line in ASS07_01:
    i += 1
    print(Line, end = '')
    Words_in_Line = len(Line.split())
    str1 = str1 + "Words in Line No: " + str(i) + " are : " + str(Words_in_Line)+"\n"
    Word_Count += Words_in_Line
    
print("\n" + str1)    
print("Total Number of words in this file are = " + str(Word_Count))

print("---------- Display each line with the words in backward order. ----------")
for Line in reversed(list(open("ASS07_01.txt"))):
    Words = Line.split()
    Reversed_Words = ' '.join(reversed(Words))
    print(Reversed_Words)

print("---------- Display line numbers of the empty lines. ----------")
print(sum(line.isspace() for line in ASS07_01), "\n")


print("---------- Display all the lines that contain alphabets and digits both. ----------")
print(sum(line.isdigit() for line in ASS07_01))
print('\n ')
print(sum(line.isalpha() for line in ASS07_01))

space_count = 0
i = 0
str2 = ""
print("---------- Display all the lines that contain only alphabets. ----------")
for line in ASS07_01:
    i+=1
    print(line, end='')
    space_in_line = len(line.split())
    str2 = str2 + " space in line is : " + str(i) + " are : " + str(space_in_line)+"\n"
    space_count+=space_in_line
    
print("\n" + str2)    

content = ASS07_01.read()
ASS07_01.close()