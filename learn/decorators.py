from functools import wraps, update_wrapper
# Decorators


def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    ''' documentation for wrapper class '''

    def __init__(self, original_function):
        self.original_function = original_function
        update_wrapper(self, original_function)

    def __call__(self, *args, **kwargs):
        print(
            f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

# def display():
#     print('display function ran')
# decorated_display = decorator_function(display)
# print("by decorated_display")
# decorated_display()


@decorator_function
def display():
    print('display function ran')


@decorator_class
def display_info(name, age):
    ''' return display info '''
    print(f'display info {name} {age}')


print("\nby decorators")
display()
display_info("girish", 20)
print(display_info.__doc__)
