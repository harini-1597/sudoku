# Sudoku using Backtracking
To solve Sudoku using the naive approach would take us 9^81 time. Which is a lot. As each box has 9 possible values, and each combination has 9 other possible combinations. 
To speed things up, we use backtracking which basically picks an empty square, tries all possible numbers while checking against validity constraints, and if the solution turns out to be wrong at a point, we backtrack, erase that number and try every possible combination.
This greatly reduces time complexity as there is pruning at each stage.

# Instructions
Ensure you have the following installed on your local machine:
- Python 3 or above
- Suitable IDE

### Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/harini-1597/sudoku.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sudoku
   ```

3. Create a Python Virtual Environment (if you use VSCode, you can create one using the Command palette itself)

    ```bash
    python3 -m venv <myenvname>
    ```

3. Install pyautogui:

   ```bash
   pip install pyautogui
   ```
4. To automate & visulaize open [Sudoku.com](https://sudoku.com/) and select a suitable difficulty level.
5. Tyoe out all the values, rowise, 0 for empty values.
6. Click on the first 1x1 box and run the script.
7. Watch how the sudoku solves itself using backtracking.

# Video Demo
https://drive.google.com/file/d/1sQ-EJVMEEazhsXYKMXjUVUnqdbuXw_en/view?usp=sharing
