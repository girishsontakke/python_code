# first class function in programming  means treating function as first class citizen entity(object)
# first class citizen entity is one which can perform all the typical functionality like assigning to
# variables, passing as parameters to function, returning function from another function

# currying means passing function as parameter or argument

def logger(tag):
    def log_message(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return log_message


log_h1 = logger("h1")
log_h1("Hello world")
print(input("enter:"))