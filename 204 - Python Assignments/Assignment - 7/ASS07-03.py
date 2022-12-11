# Q.3. Create a list of numbers. Then divide the list into 3 parts and reverse each part. Display all the parts.
def chunkify(lst, n):
    return[lst[i::n]for i in range(n)]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = chunkify(list, 3)
rev = ans[::-1]
print("Reversed list : ", rev)
print(ans)