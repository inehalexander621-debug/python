print('Mango, Orange, Pineapple, Apple, Banana')

def greet(name):
    if name:
        print(f"Hello, {name}!") # This line is indented, belonging to the if block
        print('Mango, Orange, Pineapple, Apple, Banana')
    else:
        print("Hello, stranger!") # This line is also indented, belonging to the else block
    print("Welcome to Python.") # This line is at the same indentation level as the if/else, belonging to the function but outside the conditional blocks

    