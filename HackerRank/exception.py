# Write your code here
class Calculator:
    def power(self, n, p):
        self.n = n
        self.p = p
        try:
            if n >= 0 and p >= 0:
                a = self.n ** self.p
                return a
        except:
            a = "n and p should be non-negative"
            return a   
# class e(Exception):
#     def __init__(self):
#         Exception.__init__(self,"n and p should be non-negative")

# class Calculator:
#     def power(self,n,p):
#         if  n < 0 or p < 0:
#             raise e
#         else:
#             return n**p

myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
