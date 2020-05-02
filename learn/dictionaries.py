month_conversion = {
    "jan": "january",  # only use : for equal sign
    "feb": "February",
}
print(month_conversion.get("jan"))
print(month_conversion.get("dev", "not valid "))
print(month_conversion["jan"])
print(month_conversion.values())
print(month_conversion.keys())


# Create your dictionary class
class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

    # Main Function


dict_obj = my_dictionary()

dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)
dict = {'key1': 'geeks', 'key2': 'fill_me'}
print("Current Dict is: ", dict)

# using the subscript notation
# Dictionary_Name[New_Key_Name] = New_Key_Value
dict['key2'] = 'for'
dict['key3'] = 'geeks'
print("Updated Dict is: ", dict)
dict = {'key1': 'geeks', 'key2': 'for'}
print("Current Dict is: ", dict)

# adding key3
dict.update({'key3': 'geeks'})
print("Updated Dict is: ", dict)

# adding dict1 (key4 and key5) to dict
dict1 = {'key4': 'is', 'key5': 'fabulous'}
dict.update(dict1)
print(dict)

# by assigning
dict.update(newkey1='portal')
print(dict)

dict = {'key1': 'geeks', 'key2': 'for'}

# using __setitem__ method
dict.__setitem__('newkey2', 'GEEK')
print(dict)

dict = {'a': 1, 'b': 2}

# will create a new dictionary
new_dict = {**dict, **{'c': 3}}

print(dict)
print(new_dict)
