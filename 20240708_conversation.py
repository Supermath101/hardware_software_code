def conversation(name):
    print("Hi {}".format(name.capatilize()))
    print("Welcome to my conversation program!!!")
    print("Glad to have you in Hardware & Software!!!")

def main():
    name = conversation(input("What is your name?"))
    print("Nice talking with you {}".format(name))

if __name__ == "__main__":
    main()
