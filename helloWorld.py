def greeting(name):
    print(f"Hello {name}")
    print("Have a good day")

def main():
    print("Enter your name: ", end='')
    name = input()
    greeting(name)


if __name__ == "__main__":
    main()