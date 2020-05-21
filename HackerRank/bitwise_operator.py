def max_bitwise(n, k):
    bitwise = 0
    for i in range(1, n+1):
        for j in range(i+1, n + 1):
            if bitwise < (i&j) < k:
                bitwise = (i&j)
                if bitwise == k - 1:
                    return bitwise
                
    return bitwise      

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(max_bitwise(n, k))

      
    