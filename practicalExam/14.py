# Method overloading with default arguments.

def greet(name="Guest"):
    print(f"Hello, {name}!")

print("Firstly Calling the greet() with No Argument")
greet()
print("Secondly Calling the greet() with Alice as Argument")
greet("Alice")