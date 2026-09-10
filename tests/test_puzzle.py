import numpy as np
import pytest

from environment.puzzle import SudokuPuzzle


@pytest.fixture
def puzzle_grid():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


@pytest.fixture
def solution_grid():
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]


@pytest.fixture
def sudoku_puzzle(puzzle_grid, solution_grid):
    return SudokuPuzzle(puzzle_grid, solution_grid)


def test_puzzle_creation(sudoku_puzzle, puzzle_grid, solution_grid):
    np.testing.assert_array_equal(sudoku_puzzle.puzzle, puzzle_grid)
    np.testing.assert_array_equal(sudoku_puzzle.initial_puzzle, puzzle_grid)
    np.testing.assert_array_equal(sudoku_puzzle.solution, solution_grid)


def test_empty_cell_detection(sudoku_puzzle):
    assert sudoku_puzzle.is_empty(0, 2)
    assert not sudoku_puzzle.is_empty(0, 0)


def test_correct_value_lookup(sudoku_puzzle):
    assert sudoku_puzzle.correct_value(0, 2) == 4


def test_correct_move_detection(sudoku_puzzle):
    assert sudoku_puzzle.is_correct_move(0, 2, 4)


def test_incorrect_move_detection(sudoku_puzzle):
    assert not sudoku_puzzle.is_correct_move(0, 2, 9)


def test_reset_restores_initial_puzzle(sudoku_puzzle):
    sudoku_puzzle.puzzle[0, 2] = 4

    sudoku_puzzle.reset()

    assert sudoku_puzzle.puzzle[0, 2] == 0
    np.testing.assert_array_equal(sudoku_puzzle.puzzle, sudoku_puzzle.initial_puzzle)


@pytest.mark.parametrize("shape", [(8, 9), (9, 8), (81,)])
def test_invalid_puzzle_shape_raises_value_error(shape, solution_grid):
    invalid_puzzle = np.zeros(shape, dtype=int)

    with pytest.raises(ValueError, match="puzzle must be a 9x9 grid"):
        SudokuPuzzle(invalid_puzzle, solution_grid)


def test_invalid_solution_shape_raises_value_error(puzzle_grid):
    invalid_solution = np.ones((8, 9), dtype=int)

    with pytest.raises(ValueError, match="solution must be a 9x9 grid"):
        SudokuPuzzle(puzzle_grid, invalid_solution)


@pytest.mark.parametrize("invalid_value", [-1, 10, 1.5])
def test_invalid_puzzle_values_raise_value_error(
    invalid_value, puzzle_grid, solution_grid
):
    dtype = float if isinstance(invalid_value, float) else int
    invalid_puzzle = np.array(puzzle_grid, dtype=dtype)
    invalid_puzzle[0, 0] = invalid_value

    with pytest.raises(ValueError, match="puzzle values"):
        SudokuPuzzle(invalid_puzzle, solution_grid)


@pytest.mark.parametrize("invalid_value", [0, 10, 1.5])
def test_invalid_solution_values_raise_value_error(
    invalid_value, puzzle_grid, solution_grid
):
    dtype = float if isinstance(invalid_value, float) else int
    invalid_solution = np.array(solution_grid, dtype=dtype)
    invalid_solution[0, 0] = invalid_value

    with pytest.raises(ValueError, match="solution values"):
        SudokuPuzzle(puzzle_grid, invalid_solution)
