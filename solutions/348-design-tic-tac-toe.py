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
        self.rows = [n] * n
        self.cols = [n] * n
        self.diag = n
        self.anti_diag = n
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

        diff = -1 if player == 1 else 1

        self.rows[row] += diff
        self.cols[col] += diff

        if row == col:
            self.diag[row] += diff

        if row == self.n - col - 1:
            self.anti_diag[row] += diff

        if self.rows[row] == 0 or \
            self.rows[row] == self.n * 2 or \
                self.cols[col] == 0 or self.cols[col] == self.n*2 or \
                    self.diag[row] == 0 or self.diag[row] == self.n*2 or \
                        self.anti_diag[row] == 0 or self.anti_diag[row] == self.n*2:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

# 0 1
# 0 0
