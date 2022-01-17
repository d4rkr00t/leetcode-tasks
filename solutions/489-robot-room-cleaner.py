# Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/
# hard
#
# Tags: Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


class Robot:
    def move(self):
        """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

    def turnLeft(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

    def turnRight(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

    def clean(self):
        """
       Clean the current cell.
       :rtype void
       """


def cleanRoom(robot: Robot):
    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(cell=(0, 0), d=0):
        visited.add(cell)
        robot.clean()

        for i in range(4):
            new_d = (d + i) % 4
            new_cell = (cell[0] + dir[new_d][0], cell[1] + dir[new_d][1])

            if not new_cell in visited and robot.move():
                backtrack(new_cell, new_d)
                go_back()

            robot.turnRight()

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    backtrack()