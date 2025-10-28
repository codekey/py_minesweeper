# Py Mine Sweeper
A Python CLI remake of the classic Windows Minesweeper game.
It’s an honest, beginner-friendly project created to inspire my daughter,
her high-school friends, and other aspiring Python learners.

## How to use
1. Download `py_minesweeper.py` script
1. Make sure you have Python3 installed
1. Execute `pip install colorama`. The program should work even without this module. But, this gives additional compatibility across multiple OS.
1. Execute the script as
   1. `python3 py_minesweeper.py` if you want to use default configs  OR
   1. `python3 py_minesweeper.py num_rows num_cols num_mines` if you want to configure the rows, columns and number of mines
      1. Example `python3 py_minesweeper.py 5 4 7`
1. Follow the instructions:
   1. To step on a cell, enter its number (counting starts from the top-left corner).
   1. To flag a cell as a mine, enter a negative sign followed by the cell number (for example, -4).
   1.	Each time you step on a cell:
      1. If it’s safe - you’ll see the number of neighboring mines, or ‘X’ if none are nearby.
   	1.	If you step on a cell that contains a mine - Game Over!
   1. Successfully flag all mines and reveal all other cells to win the game! 
   
