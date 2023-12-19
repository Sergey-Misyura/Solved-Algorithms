"""
661. Image Smoother
(Easy complexity)
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
"""


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        ans = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):

                total, count = 0, 0
                for delta_row in range(-1, 2):
                    for delta_col in range(-1, 2):
                        cur_row, cur_col = row + delta_row, col + delta_col
                        if rows > cur_row >= 0 and cols > cur_col >= 0:
                            total += img[cur_row][cur_col]
                            count += 1

                ans[row][col] = total // count

        return ans