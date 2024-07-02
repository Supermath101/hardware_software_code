import importlib as _importlib
n1 = _importlib.import_module("20240702_my_name2")
del _importlib

def main():
    print("Welcome to my name2 program")
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")

    n1.get_largest(num1, num2)

if __name__ == "__main__":
    main()
