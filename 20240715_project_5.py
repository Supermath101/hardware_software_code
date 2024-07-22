"""Matthew Hirsch's Project 5

This project will ask users whether they want to convert binary to decimal,
or decimal to binary. Then it'll wait for the user to type in thier input,
calculate it in the other form, and output that to the screen.
"""

import math
import curses

menu_choices = [
    ("Convert binary to decimal", "ask_bin_to_dec"),
    ("Convert decimal to binary", "ask_dec_to_bin"),
    ("Quit", None),
]

invalid_input_msg = "Invalid input recieved. Press any key to continue."

def ask(stdscr, msg):
    stdscr.erase()
    stdscr.addstr(0,0,msg + ": ")
    stdscr.move(0, len(msg) + 2)
    stdscr.refresh()
    curses.echo()
    asked_str = stdscr.getstr()
    curses.noecho()
    return str(asked_str, encoding="utf-8")

def print_and_wait(stdscr, msg):
    y, _ = stdscr.getyx()
    stdscr.insertln()
    stdscr.insstr(y + 1, 0, msg)
    stdscr.getch()

def bin_to_dec(bin):
    multiplier = 1
    accumulator = 0
    for bin_digit in reversed(bin):
        match bin_digit:
            case "1":
                accumulator += multiplier
            case "0":
                pass
            case _:
                raise Execption
        multiplier *= 2
    return str(accumulator)

def dec_to_bin(dec):
    dec = int(dec)
    bin = ""
    while dec > 0:
        bin += str(dec % 2)
        dec = int(dec / 2)
    if bin == "":
        bin = "0"
    return bin[::-1]

def is_valid_bin(bin):
    if len(bin) == 0:
        return False
    for char in bin:
        match char:
            case "0":
                pass
            case "1":
                pass
            case _:
                return False
    return True

def is_valid_dec(dec):
    if len(dec) == 0:
        return False
    for char in dec:
        match char:
            case "0":
                pass
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case _:
                return False
    return True

def ask_bin_to_dec(stdscr):
    msg = ask(stdscr, "Insert a binary number")
    if not is_valid_bin(msg):
        print_and_wait(stdscr, "{} Your input was: \"{}\"".format(invalid_input_msg, msg))
        return "main_menu"
    print_and_wait(stdscr, "The decimal equivalent is: {}".format(bin_to_dec(msg)))
    return "main_menu"

def ask_dec_to_bin(stdscr):
    msg = ask(stdscr, "Insert a decimal number")
    if not is_valid_dec(msg):
        print_and_wait(stdscr, "{} Your input was: \"{}\"".format(invalid_input_msg, msg))
        return "main_menu"
    print_and_wait(stdscr, "The binary equivalent is: {}".format(dec_to_bin(msg)))
    return "main_menu"

def print_main_menu(stdscr, selection_idx):
    stdscr.erase()
    for idx, (display, _) in enumerate(menu_choices):
        stdscr.addstr(idx, 0, display)
        if idx == selection_idx:
            stdscr.insstr(idx, 0, "* ")

def main_menu(stdscr):
    selection_idx = 0
    print_main_menu(stdscr, selection_idx)
    while True:
        match stdscr.getkey():
            case "KEY_DOWN":
                selection_idx = min(selection_idx + 1, len(menu_choices) - 1)
                print_main_menu(stdscr, selection_idx)
            case "KEY_UP":
                selection_idx = max(selection_idx - 1, 0) 
                print_main_menu(stdscr, selection_idx)
            case "\n":
                break
    (_, menu_choice_func) = menu_choices[selection_idx]
    return menu_choice_func

def main(stdscr):
    next_menu = "main_menu"
    while True:
        next_menu = globals()[next_menu](stdscr)
        if next_menu is None:
            break

if __name__ == "__main__":
    curses.wrapper(main)
