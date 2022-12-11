# Q.6. Write a Python program to take input of a string from the user and then create a dictionary
# containing each character of the string along with their frequencies. (e.g. if the string is ‘banana’
# then output should be {'b': 1, 'a': 3, 'n': 2}.

Data = input("Enter String : ")
Frequency = {}
for i in Data :     #Count frequency word by word
    if i in Frequency :
        Frequency[i] += 1
    else :
        Frequency[i] = 1
print(str(Frequency))    