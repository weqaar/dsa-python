import random


class Minesweeper:
    def __init__(self, rows=2, cols=3, num_mines=3):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = []
        self.place_mines()

    def place_mines(self):
        while len(self.mine_positions) < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) not in self.mine_positions:
                self.mine_positions.append((r, c))
                self.grid[r][c] = 1

    def find_mine(self):
        return self.mine_positions

    def move_mine(self, from_coord, to_coord):
        if from_coord in self.mine_positions:
            self.mine_positions.remove(from_coord)
            self.mine_positions.append(to_coord)
            self.grid[from_coord[0]][from_coord[1]] = 0
            self.grid[to_coord[0]][to_coord[1]] = 1
            return True
        return False

    def verify_mine_on_path(self, path):
        return any(coord in self.mine_positions for coord in path)

    def verify_mine_on_coordinate(self, coord):
        return coord in self.mine_positions

    def verify_any_mine_exists(self):
        return len(self.mine_positions) > 0, len(self.mine_positions)


# Example usage
minesweeper = Minesweeper()
print("Initial Mines:", minesweeper.find_mine())
print("Move Mine:", minesweeper.move_mine((0, 0), (1, 1)))
print("Verify Mine on Path:", minesweeper.verify_mine_on_path([(0, 0), (1, 1)]))
print("Verify Mine on Coordinate:", minesweeper.verify_mine_on_coordinate((1, 1)))
print("Verify Any Mine Exists:", minesweeper.verify_any_mine_exists())
