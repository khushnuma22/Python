# Q.6. Consider a list of characters (characters may be alphabets, special characters, digits). Write
# a Python program to do the following:
# 1) Count total number of elements in the list
# 2) Count total number of vowels in the list (vowels are ‘a’, ‘e’, ‘i’, ‘o’, ‘u’)
# 3) Count total number of consonants in the list (a consonant is an alphabet other
# than vowel)
# 4) Count total number of characters other than vowels and consonants
# Display all the values with appropriate titles

Str1 = input("Enter Any String : ")
Alphabets = Digits = Special = VCount = CCount= 0
for i in range(len(Str1)):
    if((Str1[i] >= 'a' and Str1[i] <= 'z') or (Str1[i] >= 'A' and Str1[i] <= 'Z')):
        Alphabets = Alphabets + 1
        if Str1[i] in ('a',"e","i","o","u","A","E","I","O","U"):
            VCount = VCount + 1
        elif ((Str1[i] >= 'a' and Str1[i] <= 'z') or (Str1[i] >= 'A' and Str1[i] <= 'Z')):
            CCount = CCount + 1
    elif(Str1[i] >= '0' and Str1[i] <= '9'):
        Digits = Digits + 1
    else:
        Special = Special + 1
total = Alphabets + Digits + Special
print("")
print("\n1. Total Number of Elements in this list is : ", total)
print("\n2. Total Number of Vowels in this list is : ", VCount)
print("\n3. Total Number of Vonsonants in this list is : ", CCount)
print("\n4. TOtal Number of Numbers in this List is : ", Digits)
print("\n5. Total Number of Special character other than vowel, constant and Digits : ", Special)
