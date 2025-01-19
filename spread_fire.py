import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    neighbors=[]
    grid_size = len(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
              
              if j-1>=0:
               neighbors.append(grid[i][j-1])
              if j+1<grid_size:
               neighbors.append(grid[i][j+1])
              if i-1>=0:
               neighbors.append(grid[i-1][j])
              if i+1<grid_size:
               neighbors.append(grid[i+1][j])       
              if 2 in neighbors:
               update_grid[i][j] = 2

    return update_grid


