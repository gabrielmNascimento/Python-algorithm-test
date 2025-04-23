from typing import List, Tuple

def lake_areas(matrix: List[List[int]]) -> List[int]:
    def dfs(x: int, y: int) -> int:
        # Check bounds and if the cell is part of a lake
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] == 0:
            return 0
        
        # Mark the cell as visited
        matrix[x][y] = 0
        size = 1  # Current cell contributes to the lake size

        # Explore all 8 possible directions (up, down, left, right, and diagonals)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            size += dfs(x + dx, y + dy)
        
        return size

    lake_sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:  # Found a new lake
                lake_sizes.append(dfs(i, j))
    
    lake_sizes.sort()
    return lake_sizes


if __name__ == '__main__':
    matrix = [
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0]
    ]
    print(lake_areas(matrix))