pos = -1
def swap(x, p, q):
    x[p], x[q] = x[q], x[p]
   

def sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j+1)
    return lst


ar = [10, 3, 6, 4, 25, 5, 85, 0]
p = sort(ar)
print(p)


def find_element(lst2, n):
    lower = 0
    u = len(lst2) - 1
    while lower <= u:
        mid = (lower + u) // 2
        if lst2[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst2[mid] > n:
                u = mid - 1
            else:
                lower = mid + 1
    return False


m = int(input("Find element in list : "))
if find_element(p, m):
    print("Element is at", pos + 1)
else:
    print("Element is not present")
