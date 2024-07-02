def get_largest(largest, value):
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    print("The largest value is {}".format(largest))

def main():
    print("Welcome to my name1 program")
    get_largest(7,10)

if __name__ == "__main__":
    main()
