# Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.hr = [0] * n
        self.vr = [0] * n
        self.d1r = 0
        self.d2r = 0
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
        score = 1 if player == 1 else -1
        self.hr[row] += score
        self.vr[col] += score

        if row == col:
            self.d1r += score

        if col == self.n-row-1:
            self.d2r += score

        target = self.n * score
        if self.hr[row] == target or self.vr[col] == target or self.d1r == target or self.d2r == target:
            return player

        return 0

        # Your TicTacToe object will be instantiated and called as such:
        # obj = TicTacToe(n)
        # param_1 = obj.move(row,col,player)
