# Q.5. Write a Python program to create a file containing student records where each record contain
# rollno and marks in 3 subjects separated by a comma (marks to be considered as list of 3 values).
# e.g. records of students: 1, [45, 40, 35], 2, [41, 38, 39], 3, [35, 30, 37] (each line of the file
# containing record of only 1 student). Prepare mark list in the following format:
# Roll No. Mark-1 Mark-2 Mark-3 Total
# 1        45     40     35     120

ASS04_05 = open("ASS04_05.txt", "a")
Student = {}
while True :
    Roll_no = int(input("Enter Roll_No or 0 for Exit : "))
    if Roll_no == 0 :
        break
    else :
        Total = 0
        ASS04_05.write(str(Roll_no) + "         ")
        Temp_List = []

        Math = int(input("Enter Mathematics subject mark : "))
        ASS04_05.write(str(Math) + "     ")
        Temp_List.append(Math)
        Total = Total + Math

        Eng = int(input("Enter English Subject mark : "))
        ASS04_05.write(str(Eng) + "    ")
        Temp_List.append(Eng)
        Total = Total + Eng

        Com = int(input("Enter Computer Subject Mark : "))
        ASS04_05.write(str(Com) + "    ")
        Temp_List.append(Com)
        Total = Total + Com

        ASS04_05.write(str(Total) + "\n")

        Student[Roll_no] = Temp_List
        print("\n")
ASS04_05.close()

ASS04_05 = open("ASS04_05.txt", "r")
print(ASS04_05.read())
ASS04_05.close()