class MyClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        return f"Hello, {self.name}!"


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


if __name__ == '__main__':
    # Perform some tests
    my_object = MyClass("Alice")
    print(my_object.get_name())
    print(my_object.greet())
    print(add_numbers(2, 3))
    print(multiply_numbers(4, 5))
