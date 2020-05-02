class person:
    def __init__(self, name, gpa, is_good):
        self.Id = name
        self.marks = gpa
        self.evaluation = is_good


student1 = person("Girish", 10, True)
# print(student1.name())   Error because name attribute is not given to student1
print(student1.Id)
