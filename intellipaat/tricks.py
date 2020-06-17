#Ternary Condition

condition = True

x = 1 if condition else 0

print(x)

num1 = 10_000_000
num2 = 10000000000

total = num1 + num2

print(f'{total:,}')

#use context manager 
with open('test.txt', 'r') as f:
    file_contests = f.read()

word = file_contests.split(' ')
word_count = len(word)
print(word_count)

# enumerate 
names = ['Girish', 'Carry', 'Harry', 'Cherry']

for index, value in enumerate(names, start=1):
    print(index, "." , value)


names2 = ['Peter Parker', 'Tony stark', 'Clark Kent']
heroes = ['Spiderman', 'Ironman', 'Superman']

for name, hero in zip(names2, heroes):
    print(f'{name} is actually {hero}')

for value in zip(names2, heroes):
    print(value)

# Unpacking

a, _ =  (1, 2)

print(a)
# print(b)

a, b, *c = (1,2,3,4,5)
print(a)
print(b)
print(c)


a, b, *_ = (1,2,3,4,5)
print(a)
print(b)

a, b, *c, d = (1,2,3,4,5)
print(a)
print(b) 
print(c)
print(d)

# Set attr and get attr
class Person:
    pass

person = Person()

first_key = 'first'
first_val = 'Girish'

# person.first_key = first_val
# print(person.first_key)

setattr(person, first_key, first_val)
first = getattr(person, first_key)


print(1, person.first)
print(2, first)

person1 = Person()

person_info = {'first': 'Girish', 'last':'Sontakke'}

for key, val in person_info.items():
    setattr(person1, key, val)

print(3, person1.first)
print(4, person1.last)

for key in person_info.keys():
    print(getattr(person1, key))


from getpass import getpass
# Password Input
username = input('Username: ')
Password = getpass('Password: ')

print("your password is", Password)