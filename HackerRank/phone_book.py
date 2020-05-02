# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = dict()


def add(self, keys, values):
    self[keys] = values


for i in range(n):
    y = list(input().rstrip().split())[:2]
    add(d, y[0], int(y[1]))

for i in range(n):
    try:
        x = input()
        if x in d.keys():
            print(x + "={}".format(d.get(x)))
        else:
            print("Not found")
    except:
        break
