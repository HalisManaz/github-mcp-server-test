def say_hello_world():
    """
    Print a hello world greeting to the console.
    """
    print("Hello, World!")


def say_hello_to(name):
    """
    Print a personalized greeting to the console.

    Args:
        name (str): The name of the person to greet
    """
    print(f"Hello, {name}!")


def say_goodbye():
    """
    Print a goodbye message to the console.
    """
    print("Goodbye, World!")


def main():
    """
    Main function that executes the program workflow.
    Calls the greeting and goodbye functions in sequence.
    """
    say_hello_world()
    say_hello_to("John")
    say_goodbye()


if __name__ == "__main__":
    main()
