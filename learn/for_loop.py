friends = ["Girish", "Abhishek", "kartik"]
for friend in friends :
    print(friend)
for index in range(len(friends)):
    print(index)
    print(friends[index])
base_no = int(input("Enter a base no."))
pow_no = int(input("Enter a power no."))
def raise_to_power (base_no, pow_no):
    result =1
    for index in range(pow_no):
        result = result*base_no
    return result

print(raise_to_power(base_no, pow_no))
