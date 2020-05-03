def miniMaxSum(arr):
    li = []
    for i in range(len(arr)):
        su = 0
        for j in range(len(arr)):
            su += arr[j]
        li.append(su - arr[i])
    print(min(li), max(li))
    print(li)


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
