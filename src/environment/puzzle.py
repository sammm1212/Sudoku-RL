"""Representation of a Sudoku puzzle and its solution."""

import numpy as np


class SudokuPuzzle:
    """Store the current, initial, and solved states of a Sudoku puzzle."""

    def __init__(self, puzzle, solution):
        puzzle_array = np.asarray(puzzle)
        solution_array = np.asarray(solution)

        self._validate_grid(puzzle_array, "puzzle", 0, 9)
        self._validate_grid(solution_array, "solution", 1, 9)

        self.initial_puzzle = puzzle_array.astype(np.int8, copy=True)
        self.puzzle = self.initial_puzzle.copy()
        self.solution = solution_array.astype(np.int8, copy=True)

    @staticmethod
    def _validate_grid(grid, name, minimum, maximum):
        if grid.shape != (9, 9):
            raise ValueError(f"{name} must be a 9x9 grid")
        if not np.issubdtype(grid.dtype, np.integer):
            raise ValueError(f"{name} values must be integers")
        if np.any((grid < minimum) | (grid > maximum)):
            raise ValueError(
                f"{name} values must be between {minimum} and {maximum}"
            )

    def is_empty(self, row, col):
        """Return whether the current cell is empty."""
        return self.puzzle[row, col] == 0

    def correct_value(self, row, col):
        """Return the solved value for a cell."""
        return self.solution[row, col]

    def is_correct_move(self, row, col, value):
        """Return whether a value matches the solution at a cell."""
        return self.solution[row, col] == value

    def reset(self):
        """Restore the puzzle to its initial state."""
        self.puzzle = self.initial_puzzle.copy()
