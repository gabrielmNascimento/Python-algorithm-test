Lake Areas Calculator

This project calculates the sizes of "lakes" (connected groups of `1`s) in a given 2D matrix. It uses a Depth-First Search (DFS) algorithm to traverse the matrix and determine the size of each lake.

Features
- Efficient DFS-based algorithm to calculate lake sizes.
- Handles diagonal connections between cells.
- Returns a sorted list of lake sizes.

Revamp Details
This project was recently revamped to improve its readability, performance, and maintainability:
- Simplified Logic: The DFS traversal ensures that each cell is visited only once, reducing complexity.
- Improved Readability: Clearer variable names and concise logic make the code easier to understand.
- Optimized Performance: The algorithm is efficient with a time complexity of O(N × M), where N and M are the dimensions of the matrix.

How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure you have Python 3 installed. You can check your Python version with:
   ```bash
   python3 --version
   ```

3. Run the script:
   ```bash
   python3 main2.py
   ```

4. The program will output the sizes of the lakes in the matrix. For example:
   ```
   [1, 1, 1, 2, 15]
   ```

Example Input and Output
Input Matrix:
```python
[
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0]
]
```

Output:
```
[1, 1, 1, 2, 15]
```

## How It Works
1. The program scans the matrix for cells with a value of `1`.
2. When a `1` is found, it initiates a DFS to explore all connected cells (including diagonals).
3. The size of the connected group is calculated and added to the list of lake sizes.
4. The list of lake sizes is sorted and returned.

Requirements
- Python 3.6 or higher.

Future Improvements
- Add support for larger matrices by optimizing memory usage.
- Implement a graphical representation of the lakes.
- Add unit tests for better reliability.

Author
Gabriel
```

This README provides clear instructions on how to run the project, explains the revamp, and includes an example for better understanding. Let me know if you'd like to add anything else!

Similar code found with 1 license type
