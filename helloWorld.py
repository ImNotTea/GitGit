def greeting(name):
    print(f"Hello {name}")

def main():
    print("Enter your name: ", end='')
    name = input()
    greeting(name)

if __name__ == "__main__":
    main()