# Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.d1 = 0
        self.d2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        score = -1 if player == 2 else 1
        self.rows[row] += score
        self.cols[col] += score
        if row == col:
            self.d1 += score

        if row == self.n - col - 1:
            self.d2 += score

        if any([el == self.n for el in [abs(self.rows[row]), abs(self.cols[col]), abs(self.d1), abs(self.d2)]]):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
