# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")


## ....
name = input("What's your name? ")
hello()
print(name)

## ...
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)


## ...
# Create our own function
# default value
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()


# .. main

def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)

main()

# .. 