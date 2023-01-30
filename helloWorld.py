def greeting(name):
    print(f"Hello {name}")
    print("Have a good day")
    print("I love you")
    print("You are great")

def getAge(yob):
    return 2023 - int(yob)

def main():
    print("Enter your name: ", end='')
    name = input()
    greeting(name)


if __name__ == "__main__":
    main()