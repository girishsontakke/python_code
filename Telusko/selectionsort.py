def swap(x, p, q):
    x[p], x[q] = x[q], x[p]

    
def sort(lst):
    for i in range(len(lst)):
        minpos = i
        for j in range(i, len(lst)):
            if lst[minpos] > lst[j]:
                minpos = j

        swap(lst, i, minpos)

    return lst


so = [10, 3, 6, 4, 25, 85, 0, 5]
p = sort(so)
print(p, "This is sorted list")
