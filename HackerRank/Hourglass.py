import numpy as np

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
# print(arr)
hg1 = []
for row in range(4):
    c = []
    for col in range(4):
        r = []
        for i in range(col, col + 3):
            r.append(arr[row][i])
        c.append(r)
    hg1.append(c)

print("hg1")
for _ in range(4):
    print(hg1[_])
hg2 = []
for row in range(1, 5):
    c = []
    for col in range(4):
        r = []
        for i in range(col, col + 3):
            if i == col + 1:
                r.append(arr[row][i])
            else:
                r.append(0)
        c.append(r)
    hg2.append(c)

print("hg2")
for _ in range(4):
    print(hg2[_])

hg3 = []
for row in range(2, 6):
    c = []
    for col in range(4):
        r = []
        for i in range(col, col + 3):
            r.append(arr[row][i])
        c.append(r)
    hg3.append(c)

print("hg3")
for _ in range(4):
    print(hg3[_])

hg = []
for x in range(4):
    hg_n = []
    for y in range(4):
        hg_m = []
        for z in range(y, 4):
            hg_m.append(hg1[x][y])
            hg_m.append(hg2[x][y])
            hg_m.append(hg3[x][y])
            break
        hg_n.append(hg_m)
    hg.append(hg_n)
print("hg")
for _ in range(4):
    print(hg[_])

print(np.sum(hg[0][0]))
ad = []
for p in range(4):
    for q in range(4):
        ad.append(sum(map(sum, hg[p][q])))
print(ad)
print(max(ad))
