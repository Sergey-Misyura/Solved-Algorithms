"""
1496. Path Crossing
(Easy complexity)

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        coords = set()
        coords.add((x, y))

        for direction in path:
            if direction == 'N' or direction == 'S':
                y += 1 if direction == 'N' else -1
            else:
                x += 1 if direction == 'E' else -1

            if (x, y) in coords:
                return True
                break

            coords.add((x, y))

        return False