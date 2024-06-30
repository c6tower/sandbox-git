import sys


def hello_world(name: str):
    print(f"Hello, {name}!")


def goodbye_world(name: str):
    print(f"Goodbye, {name}!")


def main():
    name = "world"
    if len(sys.argv) < 1:
        print("Usage: python hoge.py [name]")
        raise SystemExit(1)
    else:
        name = sys.argv[1]

    hello_world(name)
    goodbye_world(name)


if __name__ == "__main__":
    main()
