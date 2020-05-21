friends = "me"
lst = ["apple", "mango", 2, 5, friends]
print(lst)
lst.append("father")
print(lst)
list2 = ["art"]
lst.extend(list2)
lst.insert(2, "banana")
print(lst)
print(lst[1:4])
m = lst.index("apple")
print(m)
print(lst[3])
print("index of apple = ", lst.index("apple") + 1)
print("turtle" in lst)
lst.remove("apple")
print(lst)
