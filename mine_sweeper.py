import os
import random
import time

# GLOBAL VARIABLES
minescape, exposed, flags = [], [], []
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
            minescape.append((r, c))
        i += 1
    minescape.sort()


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

def flag_mine(i, j):
    flags.append((i,j))

def draw_minefield(l, w, final=False, cheat=False):
    os.system('clear')
    print("\n\n** Minesweeper **")
    print("+---" * w + "+")
    for i in range(l):
        for j in range(w):
            print("|", end="")
            if True in (final, cheat) and (i, j) in minescape:
                print("💣 ", end="")
            elif (i, j) in exposed:
                print(f"{count_neighbor_mines(i,j):^3s}", end="")
            else:
                print("   ", end="")
        print("|")
        print("+---" * w + "+")
    # print(minescape)
    # print(exposed)


def boom(r, c):
    if (r, c) in minescape:
        return True
    else:
        return False

def validate():
    pass


def main():
    l, w, num_mines = 5, 5, 1
    minescape = lay_mines(l, w, num_mines)
    # print(minescape)
    while True:
        draw_minefield(l, w)
        print("\n")
        ch = input(f"Enter 1 - {l*w} for cell with no mine (q for exit): ")
        if ch == 'q':
            break
        elif ch == "ch":
            draw_minefield(l, w, cheat=True)
            time.sleep(3)
            continue

        try:
            ch = int(ch) - 1 	
            # Converting to Array index as user enters 1 to n
            r, c = ch // w, ch % w
        except ValueError:
            print(f"Enter either a number 1 - {l*w} OR q for exit.")
            time.sleep(3)
            continue
        if boom(r, c):
            draw_minefield(l, w, final=True)
            print("🔥 BLAAST..!!!! 🔥\n\n")
            break
        else:
            exposed.append((r, c))


if __name__ == "__main__":
    main()
