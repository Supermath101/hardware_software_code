from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        system('clear')

def while_loop(my_loop):
    counter = 0
    while counter < len(my_loop):
        print(my_loop[counter])
        counter += 1

def for_loop(my_loop):
    for one_item in my_loop:
        print(one_item)

def my_msg(loop_type):
    print("#" * 12)
    print("Running {} loop".format(loop_type))

def main():
    lang_list = [
        "Python", "JavaScript", "PHP",
        "Rust", "Java", "Assembly",
    ]
    clear_screen()
    my_msg("for")
    for_loop(lang_list)
    my_msg("while")
    while_loop(lang_list)

if __name__ == "__main__":
    main()
