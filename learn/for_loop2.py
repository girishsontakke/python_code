T = int(input("Enter a No of Strings : "))
S = []
for i in range(T):
    S.append(input("Enter the string : "))
    
    
for j in range(len(S)):
    temp = str(S[j])
    for k in range(len(temp)):
        if k % 2 == 0:
            print(temp[k], end="")
    print(end = " ")
    
    for k in range(len(temp)):
        if k % 2 != 0:
            print(temp[k], end="")
    print(end = "\n")
