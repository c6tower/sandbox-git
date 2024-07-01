import sys


def hello_world(name: str):
    print(f"Hello, {name}!")


def goodbye_world(name: str):
    print(f"Goodbye, {name}!")


def main():
    name = "world"

    hello_world(name)
    goodbye_world(name)


if __name__ == "__main__":
    main()
