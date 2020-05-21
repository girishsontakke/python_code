n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
number = 0
for i in range(n):
    numSwaps = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numSwaps += 1
            number += 1
    print(a)
    if numSwaps == 0:
        break

print("Array is sorted in", number, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a) - 1])