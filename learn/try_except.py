try:
        number=10/0
        num=int(input("Enter a number"))
        
except ZeroDivisionError:
        print("divided by zero")
except ValueError:
        print("Invalid type")
