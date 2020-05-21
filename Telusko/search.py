lst = [1, 2, 3, 4, 5, 6, 7]
n = int(input("Enter a number to be searched in list: "))
count = 0

for i in range(len(lst)):
    if lst[i] == n:
        count += 1

if count != 0:
    print(str(n) + " is in list")
else:
    print(str(n) + " is not in list")
