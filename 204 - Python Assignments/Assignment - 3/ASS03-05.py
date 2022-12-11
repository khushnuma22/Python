# Q.5. Write a Python program to create a dictionary of student data by taking input from the user,
# where each student data contains Rollno (to be considered as key), and marks in 3 subjects (to
# be considered as list of values). e.g. {1 : [45, 40, 35], 2 : [41, 38, 39], 3 : [35, 30, 37]}. Prepare
# mark list in the following format:
# Roll No. Mark-1 Mark-2 Mark-3 Total
# 1           45    40     35    120

Student = {}
while True :
    Roll_no = int(input("Enter Roll_No or 0 for Exit : "))
    if Roll_no == 0 :
        break
    else :
        Temp_List = []
        Math = int(input("Enter Mathematics subject mark : "))
        Temp_List.append(Math)
        Eng = int(input("Enter English Subject mark : "))
        Temp_List.append(Eng)
        Com = int(input("Enter Computer Subject Mark : "))
        Temp_List.append(Com)
        Student[Roll_no] = Temp_List
        print("\n")

print("Roll No.  Math   Eng   Com   Total")
for i in Student :
    Temp_List1 = []
    total = 0
    Temp_List1.append(i)
    for j in Student[i] :
        Temp_List1.append(j)
        total = total + j
    print(Temp_List1[0], "       ", Temp_List1[1], "   ", Temp_List1[2], "  ", Temp_List1[3], "  ", total)