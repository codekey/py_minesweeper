"""
py_minesweeper - a Python CLI remake of the classic Windows Minesweeper game.
It’s an honest, beginner-friendly project created to inspire my daughter, 
her high-school friends, and other aspiring Python learners.
"""

import os, sys
import random, time
from colorama import Fore, Back, Style


# GLOBAL VARIABLES: 
# Configurable ASCII for graphic's
mine, red_flag, fire = 128163, 128681, 128293

# Not for configuring. Do not modify.
minescape, exposed, flags = set(), set(), set()



def lay_mines(l, w, m):
# Generates random mines and assigns locations
    i, taken = 0, []
    while i < m:
        rnd = random.randint(1, l*w)
        if rnd in taken:
            continue
        else:
            taken.append(rnd)
            r, c = rnd // w, rnd % w
            minescape.add((r, c))
        i += 1


def count_neighbor_mines(i, j):
# Finds the number of mines in neighboring cells for a given cell
    count = 0
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if r == i and c == j:
                continue
            if r < 0 or c < 0:
                continue
            if (r, c) in minescape:
                count += 1
    return str(count) if count > 0 else " X "

def step_on(r, c):
# Player decided to step on the given cell
    exposed.add((r, c))
    if (r, c) in flags:
        flags.remove((r, c))

def flag_mine(r, c):
# Player decided to flag the given cell
    flags.add((r, c))
    if (r, c) in exposed:
        exposed.remove((r, c))

def draw_minefield(l, w, final=False, cheat=False):
# Draws the minefield
    os.system('clear')
    print(Fore.BLUE + Style.BRIGHT + \
    "\n\n**** Py Mine-Sweeper ****" + Style.RESET_ALL)
    print(Style.BRIGHT + "+---" * w + "+" + Style.RESET_ALL)
    for i in range(l):
        for j in range(w):
            print(Style.BRIGHT + "|" + Style.RESET_ALL, end="")
            if True in (final, cheat) and (i, j) in minescape:
                print(f"{chr(mine)} ", end="")
            elif (i, j) in flags:
                print(f" {chr(red_flag)}", end="")
            elif (i, j) in exposed:
                print(Style.BRIGHT + f"{count_neighbor_mines(i,j):^3s}" + Style.RESET_ALL, end="")
            else:
                print("   ", end="")
        print(Style.BRIGHT + "|")
        print(Style.BRIGHT + "+---" * w + "+" + Style.RESET_ALL)

def boom(r, c):
# Just stepped on a mine or not? Defined function to give room for future additions
    if (r, c) in minescape:
        return True
    else:
        return False

def calculate(ch, l, w):
# Convert the single number input to the choice of step-on vs flag and row & col
    flg = False
    try:
        ch = int(ch)
        if ch < 0:      # if User chose to Flag and not Expose
            flg = True
            ch = abs(ch)
        ch = ch - 1
        r, c = ch // w, ch % w # Converting to Array index as user enters 1 to n
    except (TypeError, ValueError):
        r = c = -1
        print(Fore.YELLOW + f"Enter either a number 1 - {l*w} OR q for exit." + \
        Style.RESET_ALL)
        time.sleep(3)
    return r, c, flg 

def won():
# Find if the player has won. Defined function to give room for future additions
    if flags == minescape:
        return True
    else:
        return False 

def main():
    l, w, num_mines = 4, 4, 3
    if len(sys.argv) >= 3: 
        l = int(sys.argv[1].strip())
        w = int(sys.argv[2].strip())
        num_mines = int(sys.argv[3].strip())
    area = l * w
    minescape = lay_mines(l, w, num_mines)

    while True:
        draw_minefield(l, w)
        print("\n")
        if (len(exposed) + len(flags)) >= area: # if all cells are taken, check if player has won!
            if won():
                print(f"Amazing! You won the game!!\n\n") 
                break

        print(Fore.RED + Style.BRIGHT + \
        f"* Enter 1 - {l*w} for exposing a cell with no mine (Count from top-left)" + Style.RESET_ALL)
        print(Fore.GREEN + \
        f"* Enter Negative number for flagging a cell with mine" + Style.RESET_ALL)
        choice = input(Style.BRIGHT + "* Enter your choice or 'q' for exit: " + Style.RESET_ALL)

        if choice == 'q':           # Exit the game
            break
        elif choice == chr(231):    # Cheat-code!
            draw_minefield(l, w, cheat=True)
            time.sleep(2)
            continue

        r, c, flg = calculate(choice, l, w)
        if flg:
              flag_mine(r, c)
        elif boom(r, c):
            draw_minefield(l, w, final=True)
            print("\n\n" + f"{chr(fire)}"*2 + Fore.YELLOW + Style.BRIGHT + \
            " BLAAST..!!!! " + Style.RESET_ALL + f"{chr(fire)}"*2 + "\n\n")
            break
        else:
            step_on(r, c)


if __name__ == "__main__":
    main()
