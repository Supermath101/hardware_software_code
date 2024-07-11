def check_selection(hex_digits):
    hex_list = [
        "A", "B", "C", "D", "E", "F",
        "0", "1", "2", "3", "4", "5",
        "6", "7", "8", "9"
    ]
    for hex_digit in hex_digits:
        if hex_digit.upper() not in hex_list:
            input("{} is not a hexadecimal number!".format(hex_digits))
            return True
    return False

def main():
    checking_for_hex_number = True
    while checking_for_hex_number:
        selection = input("Provide a hexadecimal number: ")
        checking_for_hex_number = check_selection(selection)
    print("Good job!!\n{} is a hexadecimal number!!!".format(selection))

if __name__ == "__main__":
    main()
