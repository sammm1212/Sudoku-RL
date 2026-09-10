# Reinforcement Learning for Sudoku

This project explores reinforcement learning for solving Sudoku through
sequential interaction with an environment that gives immediate feedback.
Incorrect values receive a negative reward and are not inserted into the board.

## Research Question

Can a reinforcement learning agent learn to solve Sudoku through sequential
interaction and immediate feedback, and how do techniques such as action masking
and curriculum learning affect performance?

## Planned Formulation

- **State:** current Sudoku board
- **Action:** choose a row, column and digit
- **Reward:** positive for a correct move, negative for an incorrect move, and
  an additional reward for completing a puzzle
- **Incorrect moves:** do not alter the board

## Planned Experiments

- Random baseline
- Basic DQN
- Action masking
- Curriculum learning
- Performance across Sudoku difficulty levels
