def say_hello_world():
    print("Hello, World!")


def say_hello_to(name):
    print(f"Hello, {name}!")


def say_goodbye():
    print("Goodbye, World!")


def main():
    say_hello_world()
    say_hello_to("John")
    say_goodbye()


if __name__ == "__main__":
    main()
