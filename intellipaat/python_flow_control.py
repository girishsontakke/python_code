# for number in range(1, 101):
#   r=0
#   for i in range(2, number//2 + 1):
#     if (number % i) == 0:
#       r += 1
#       break

#   if (r == 0 and number!=1):
#     print(str(number), end=(", "))

def is_prime_no(num):
  count=0
  for i in range(2,num):
    if (num % i)== 0:
      count+=1
      break
  if count==0 and num>1:
    return True
def show():
  for i in range(1,101):
    if is_prime_no(i):
      print(str(i), end=(" "))
show()