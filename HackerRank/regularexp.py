if __name__ == '__main__':
    N = int(input())
    li = dict()
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if emailID[-10:] == '@gmail.com':
            li.update({emailID : firstName})
    
    s = list()
    for val in li.values():
        s.append(val)
    
    for i in range(len(s)-1, 0, -1):
        for j in range(i):
            if s[j]>s[j+1]:
                temp=s[j]
                s[j]=s[j+1]
                s[j+1]=temp
    
    for k in range(len(s)):
        print(s[k])
