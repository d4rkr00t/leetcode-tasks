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
    def goBack():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    visited = set()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, dir):
        robot.clean()
        visited.add((x, y))

        for i in range(4):
            nextDir = (dir + i) % 4
            xi = dirs[nextDir][0] + x
            yj = dirs[nextDir][1] + y

            if (xi, yj) not in visited and robot.move():
                dfs(xi, yj, nextDir)
                goBack()

            robot.turnRight()

    dfs(0, 0, 0)
