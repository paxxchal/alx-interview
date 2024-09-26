#!/usr/bin/python3

def island_perimeter(grid):
  """
  Calculates the perimeter of the island in a grid.

  Args:
      grid: A list of lists of integers representing a rectangular grid.
          0 represents water, 1 represents land.

  Returns:
      The perimeter of the island in the grid. 
  """
  rows, cols = len(grid), len(grid[0])
  perimeter = 0

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == 1:
        perimeter += 4  # Initial perimeter for a land cell

        # Check for adjacent land cells and subtract perimeter for edges
        if row > 0 and grid[row - 1][col] == 1:
          perimeter -= 2
        if col > 0 and grid[row][col - 1] == 1:
          perimeter -= 2

  return perimeter

# Make the script executable (optional but recommended)
if __name__ == "__main__":
  # Example usage (replace with your actual grid)
  grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
  perimeter = island_perimeter(grid)
  print("Perimeter of the island:", perimeter)
