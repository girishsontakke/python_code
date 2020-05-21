def division(a, b):
    print(a // b)


print("file open")

a = int(input("Enter divident: "))
b = int(input("Enter divisor: "))

try:
    division(a, b)
except ZeroDivisionError as e:
    print("divided by zero")
    print(e)
except ValueError as e:
    print("Invalid Input")
    print(e)
except Exception as e:
    print("something went wrong")
finally:
    print("file closed")
