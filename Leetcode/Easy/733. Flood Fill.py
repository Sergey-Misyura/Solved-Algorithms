"""
733. Flood Fill
(Easy complexity)

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to
the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        oldColor, newColor = image[sr][sc], color
        shifts = [(-1,0), (0,-1), (0,1), (1, 0)]


        def colored(image, i, j):

            if i < 0 or i > len(image) - 1:
                return
            if j < 0 or j > len(image[0]) - 1:
                return
        
            if image[i][j] != oldColor:
                return
            else:
                image[i][j] = newColor

            for shift in shifts:
                colored(image, i+shift[0], j+shift[1])

        if oldColor!= newColor:
            colored(image, sr, sc)

        return image