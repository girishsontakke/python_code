#pass by value
a = 10

def change_value(b):
    print("value of b = " + str(b))
    b = 100
    print("value of b = " + str(b))


change_value(a)
print(a)

# pass by reference 
c = [10, 20]


def change_value_2(b):
    print("value of b = " + str(b))
    b[0] = 30
    b[1] = 40
    print("value of b = " + str(b))


change_value_2(c)
print(c)
