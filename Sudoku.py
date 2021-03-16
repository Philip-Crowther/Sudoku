import random
import numpy as np


class Sudoku:
    def __init__(self):
        # here the puzzle is empty, each group of three rows is generated within its own array referred to from here on as a "superrow"
        self.puzzle = np.zeros([9, 9])
        nums = list(range(1, 10))
        random.shuffle(nums)
        self.generate(0, 0, nums)

    def print(self):
        for row in self.puzzle:
            print(row)

    def generate(self, row, col, nums):
        # row and column are self-explanatory, nums is a randomly ordered list of numbers re-initialized for each row
        # doing this with nums ensures a more random board each time

        for num in nums:
            if num not in self.puzzle[:, col] and not self.inbox(num, row, col):  # row check take care of by nums
                self.puzzle[row, col] = num

                if col == 8:  # then you are at the end of a row
                    if row == 8:  # then this end of the row is the end of the puzzle and it is complete
                        return

                    nums2 = list(range(1, 10))
                    random.shuffle(nums2)
                    self.generate(row + 1, 0, nums2)

                else:  # you just need to move one ahead
                    nums2 = nums.copy()
                    nums2.remove(num)
                    self.generate(row, col + 1, nums2)

                if self.puzzle[
                    8, 8] == 0:  # then there were no possible valid boards stemming from this num and we must test others
                    self.puzzle[row, col] = 0  # we need to reset this spot to zero so it doesn't mess up future tests
                    continue
                else:  # you've found the right one and nothing else needs to happen
                    return

    def inbox(self, num, row, col):  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if row < 3:  # [:3, x]
            if col < 3:  # [x, :3]
                return num in self.puzzle[:3, :3]
            elif col > 5:  # [x, 3:6]
                return num in self.puzzle[:3, 6:]
            else:  # [x, 6:]
                return num in self.puzzle[:3, 3:6]

        elif row > 5:  # [6:, x]
            if col < 3:  # [x, :3]
                return num in self.puzzle[6:, :3]
            elif col > 5:  # [x, 3:6]
                return num in self.puzzle[6:, 6:]
            else:  # [x, 6:]
                return num in self.puzzle[6:, 3:6]

        else:  # [3:6, x]
            if col < 3:  # [x, :3]
                return num in self.puzzle[3:6, :3]
            elif col > 5:  # [x, 3:6]
                return num in self.puzzle[3:6, 6:]
            else:  # [x, 6:]
                return num in self.puzzle[3:6, 3:6]


s = Sudoku()
s.print()
