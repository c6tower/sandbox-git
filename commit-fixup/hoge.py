import sys


def hello_world(name: str):
    print(f"Hello, {name}!")


def goodbye_world():
    print("Goodbye, world!")


def main():
    name = "world"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    
    hello_world(name)
    goodbye_world()


if __name__ == "__main__":
    main()
