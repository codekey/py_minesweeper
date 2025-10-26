import os, sys
import random
import time

# GLOBAL VARIABLES
minescape, exposed, flags = set(), set(), set()
num_selections = 0


def lay_mines(l, w, m):
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
    #minescape.sort()


def count_neighbor_mines(i, j):
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

def expose_mine(r, c):
    exposed.add((r, c))
    if (r, c) in flags:
        flags.remove((r, c))

def flag_mine(r, c):
    flags.add((r, c))
    if (r, c) in exposed:
        exposed.remove((r, c))

def draw_minefield(l, w, final=False, cheat=False):
    os.system('clear')
    print("\n\n** Minesweeper **")
    print("+---" * w + "+")
    for i in range(l):
        for j in range(w):
            print("|", end="")
            if True in (final, cheat) and (i, j) in minescape:
                print("💣 ", end="")
            elif (i, j) in flags:
                print(f" 🚩", end="")
            elif (i, j) in exposed:
                print(f"{count_neighbor_mines(i,j):^3s}", end="")
            else:
                print("   ", end="")
        print("|")
        print("+---" * w + "+")

def boom(r, c):
    if (r, c) in minescape:
        return True
    else:
        return False

def calculate(ch, l, w):
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
        print(f"Enter either a number 1 - {l*w} OR q for exit.")
        time.sleep(3)
    return r, c, flg 

def won():
    if flags == minescape:
        print(f"Amazing! You won the game!!\n\n") 
        return True
    else:
        return False 

def main():
    l, w, num_mines = 3, 3, 1
    if len(sys.argv) >= 3:
        l = int(sys.argv[1].strip())
        w = int(sys.argv[2].strip())
        num_mines = int(sys.argv[3].strip())
    area = l * w
    minescape = lay_mines(l, w, num_mines)

    while True:
        draw_minefield(l, w)
        print("\n")
        if (len(exposed) + len(flags)) >= area: # if all cells are taken, check if player won!
            if won():
                return
        print(f"* Enter 1 - {l*w} for exposing a cell with no mine (Count for top-left)")
        print(f"* Enter Negative number for flagging a cell with mine")
        ch = input("* Enter 'q' for exit: ")
        if ch == 'q':
            break
        elif ch == "ch":
            draw_minefield(l, w, cheat=True)
            time.sleep(3)
            continue
        r, c, flg = calculate(ch, l, w)
        if flg:
              flag_mine(r, c)
        elif boom(r, c):
            draw_minefield(l, w, final=True)
            print("🔥 BLAAST..!!!! 🔥\n\n")
            break
        else:
            expose_mine(r, c)


if __name__ == "__main__":
    main()
