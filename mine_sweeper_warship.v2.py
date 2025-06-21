import argparse
import random

try:
    import numpy
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


class Minesweeper:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.num_mines = 0
        self.grid = None
        self.mine_positions = []
        self.using_numpy = False

    def create_grid(self, rows=2, cols=3, num_mines=1, use_numpy=False):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.using_numpy = use_numpy and HAS_NUMPY
        if self.using_numpy:
            self.grid = numpy.zeros((rows, cols), dtype=int)
        else:
            self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.place_mines()

    def place_mines(self):
        # Ensure mine_positions is reset if create_grid is called multiple times
        self.mine_positions = []
        # Ensure num_mines does not exceed the number of cells
        if self.num_mines > self.rows * self.cols:
            print(f"Warning: Number of mines ({self.num_mines}) exceeds grid capacity ({self.rows * self.cols}). Setting mines to maximum possible.")
            self.num_mines = self.rows * self.cols
            
        while len(self.mine_positions) < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) not in self.mine_positions:
                self.mine_positions.append((r, c))
                self.grid[r][c] = 1

    def find_mine(self):
        return self.mine_positions

    def move_mine(self, from_coord, to_coord):
        # Validate coordinates
        fr, fc = from_coord
        tr, tc = to_coord
        if not (0 <= fr < self.rows and 0 <= fc < self.cols and \
                0 <= tr < self.rows and 0 <= tc < self.cols):
            print(f"Error: Invalid coordinates for move_mine. Grid is {self.rows}x{self.cols}.")
            return False
            
        if from_coord in self.mine_positions:
            # Prevent moving a mine to an already occupied mine position (unless it's itself, which is redundant)
            if to_coord in self.mine_positions and to_coord != from_coord:
                print(f"Warning: Cannot move mine from {from_coord} to {to_coord} as target is already a mine.")
                return False # Or handle as per game logic, e.g., swap if intended

            self.mine_positions.remove(from_coord)
            self.mine_positions.append(to_coord)
            self.grid[fr][fc] = 0
            self.grid[tr][tc] = 1
            return True
        print(f"Info: No mine at {from_coord} to move.")
        return False

    def verify_mine_on_path(self, path):
        if not path:
            return False
        return any(coord in self.mine_positions for coord in path)

    def verify_mine_on_coordinate(self, coord):
        return coord in self.mine_positions

    def verify_any_mine_exists(self):
        return len(self.mine_positions) > 0, len(self.mine_positions)

    def display_grid(self):
        if self.grid is None:
            print("Grid not created yet.")
            return

        print("\nGrid Display:")

        # Determine the number of digits for the widest row number for formatting.
        if self.rows > 0:
            max_row_digits = len(str(self.rows - 1))
        else:
            max_row_digits = 1 # Assumed width for '0' if no rows

        for r in range(self.rows):
            # Format row number to fixed width for alignment
            row_label = f"{r:<{max_row_digits}}  " # Row number, padded, followed by two spaces
            row_display = []
            for c in range(self.cols):
                row_display.append('M' if self.grid[r][c] == 1 else '.')
            print(row_label + " ".join(row_display))

        # Print bottom X-axis (column numbers)
        if self.cols > 0:
            # Padding to align column numbers under the grid content.
            # This accounts for the width of the formatted row label part:
            # max_row_digits for the number itself, plus 2 spaces.
            bottom_axis_padding_len = max_row_digits + 2
            padding_str = " " * bottom_axis_padding_len
            
            col_numbers_str_list = [str(c_idx) for c_idx in range(self.cols)]
            print(padding_str + " ".join(col_numbers_str_list))


def main():
    parser = argparse.ArgumentParser(description="Minesweeper CLI")
    parser.add_argument(
        "--rows", type=int, default=2, help="Number of rows in the grid"
    )
    parser.add_argument(
        "--cols", type=int, default=3, help="Number of columns in the grid"
    )
    parser.add_argument(
        "--mines", type=int, default=3, help="Number of mines in the grid"
    )
    parser.add_argument(
        "--use_numpy", action="store_true", help="Use numpy for grid creation if available"
    )
    parser.add_argument(
        "--display_grid", action="store_true", help="Display the grid after creation and operations"
    )
    args = parser.parse_args()

    if args.rows <= 0 or args.cols <= 0:
        print("Error: Number of rows and columns must be positive.")
        return
    if args.mines < 0:
        print("Error: Number of mines cannot be negative.")
        return


    if args.use_numpy and not HAS_NUMPY:
        print("Warning: NumPy is not installed. Falling back to list-based grid.")

    minesweeper = Minesweeper()
    minesweeper.create_grid(args.rows, args.cols, args.mines, use_numpy=args.use_numpy)
    
    if args.display_grid:
        minesweeper.display_grid()

    # Example usage
    print("\nInitial Mines:", minesweeper.find_mine())
    
    # Example move: try moving a mine from (0,0) if it exists, to (1,1) if valid
    # This is just an example; in a real game, 'from_coord' would be known or chosen
    example_from_coord = (0,0) 
    example_to_coord = (1,1)
    
    # Ensure example_to_coord is within bounds before attempting move
    if 0 <= example_to_coord[0] < minesweeper.rows and \
       0 <= example_to_coord[1] < minesweeper.cols:
        print(f"Attempting to move mine from {example_from_coord} to {example_to_coord}: {minesweeper.move_mine(example_from_coord, example_to_coord)}")
    else:
        print(f"Info: Example 'to_coord' {example_to_coord} is out of bounds for the current grid. Skipping move example.")

    # Example path verification
    example_path = []
    if minesweeper.rows > 1 and minesweeper.cols > 1: # Ensure path is possible
        example_path = [(0, 0), (1, 1)]
        print(f"Verify Mine on Path {example_path}: {minesweeper.verify_mine_on_path(example_path)}")
    
    # Example coordinate verification
    example_coord_verify = (1,1)
    if 0 <= example_coord_verify[0] < minesweeper.rows and \
       0 <= example_coord_verify[1] < minesweeper.cols:
        print(f"Verify Mine on Coordinate {example_coord_verify}: {minesweeper.verify_mine_on_coordinate(example_coord_verify)}")
    
    print("Verify Any Mine Exists:", minesweeper.verify_any_mine_exists())

    if args.display_grid:
        minesweeper.display_grid()


if __name__ == "__main__":
    main()
