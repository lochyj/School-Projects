# Assessment Task 3 - Challenge 2

## Info

Play the game before reading the code. It will make it slightly
easier to understand what the code is doing.

## Running

Prerequisites:

- `pygame`
- `pygame_gui`

Obtain them with:

- `py -m pip install pygame pygame_gui`

Note:
Tested on linux with python 3.11.4. It may or may not work on windows.

## Playing the game

To play the game you simply drag and drop a
number from the grid at the side to a position
on the sudoku grid for it to be placed. If the
number cannot be placed in that cell
(e.g the row already has a 3 in it and you place a 3 in that row)
then the number wont be placed. (It's a little jarring)

There are a number of options in the game. This includes enabling
cheats, removing wrong numbers from the grid and regenerating the grid.

Cheats:

- Gives the user the solution to the sudoku grid
one number at a time (overlaid on the grid)
- Prevents the user from placing any numbers in the incorrect position

Removing wrong numbers:

- Removes all of the numbers in the grid that have
been placed in the wrong position

Regenerating the grid:

- Generates a new grid

## Solvability

The game grid is generated from a fully solved grid (which we also generate) and has random cells removed.
This may mean that the game grid may not be able to be solved.
There is almost 100% a way to prevent this but
I don't have the time to research it.

However, this most likely wont happen very often.
Additionally, My Dad completed one successfully (On HARD mode) which
proves that it is in fact possible at least some of the time.

## Generating the grid

This is mostly explained in the code. But, I will comment on the process I undertook to make it.
Initially I messed around with randomly filling the grid with values that are within the rules of
sudoku. However, this produced grids that weren't fully complete and were unsolvable. After trying a
few different ways of filling the grid, I looked for a way to fill in as much of the grid as possible
without having to lots of calculations, this lead to filling the 3 diagonal squares, as they don't
interfere with each other and only require some shuffling to fill. After this, I looked into
backtracking algorithms and settled with the current generator.

## The solver

As you may notice in the code, the solver function is not a real solver but instead
just picking a random value from the initially computed grid.
I simply don't have the time to implement a real solver especially
when this is a simple task. I may implement a real solver in the future.

## Comments on functions that draw stuff to the screen

These functions really lack explanation in the code, this is because of the nature
of the function, they place text or rects places on the screen and are really
unintuitive which requires them to have lots of magic numbers that even i've
forgotten why they are there...

## American spelling

I used american spelling for most things because my spell
checker puts squiggles everywhere I use english spelling
so I just use the american spelling.
