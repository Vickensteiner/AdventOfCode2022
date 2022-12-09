import numpy as np
from scipy.sparse import csr_matrix

with open("Day 8/day8input.txt") as infile:
    lines = infile.readlines()
    for i in range(len(lines)):
        lines[i] = [int(number) for number in lines[i].strip('\n')]
    original_grid = np.array(lines).astype(int)
    vis_row = []
    vis_col = []

    for i in range(original_grid.shape[0]):
        grid = np.copy(original_grid)
        j = 0

        vis_row.append(i)
        vis_col.append(j)
        grid[i] -= grid[i, j]
        while(j < grid.shape[1] - 1):
            j += 1
            if(grid[i, j] > 0):
                vis_row.append(i)
                vis_col.append(j)
                grid[i] -= grid[i, j]
        
        grid = np.copy(original_grid)
        j = len(grid) - 1

        vis_row.append(i)
        vis_col.append(j)
        grid[i] -= grid[i, j]
        while(j > 1):
            j -= 1
            if(grid[i, j] > 0):
                vis_row.append(i)
                vis_col.append(j)
                grid[i] -= grid[i, j]

        grid = np.copy(original_grid)
        j = 0

        vis_row.append(j)
        vis_col.append(i)
        grid[:, i] -= grid[j, i]
        while(j < grid.shape[1] - 1):
            j += 1
            if(grid[j, i] > 0):
                vis_row.append(j)
                vis_col.append(i)
                grid[:, i] -= grid[j, i]

        grid = np.copy(original_grid)
        j = len(grid) - 1

        vis_row.append(j)
        vis_col.append(i)
        grid[:, i] -= grid[j, i]
        while(j > 1):
            j -= 1
            if(grid[j, i] > 0):
                vis_row.append(j)
                vis_col.append(i)
                grid[:, i] -= grid[j, i]
        
    data = np.ones(len(vis_row))
    sparse_matrix = csr_matrix((data, (vis_row, vis_col)), shape = original_grid.shape)
    sparse_matrix = np.where(sparse_matrix.toarray() > 0, 1, 0)
    print(np.sum(sparse_matrix))
# End Part 1

    best_tree_candidates = []
    for i in range(1, len(original_grid) - 2):
        for j in range(1, len(original_grid[0]) - 2):
            best_tree_candidates.append((i, j))

    best_score = 0
    for candidate in best_tree_candidates:
        i, j = candidate[0], candidate[1]
        scores = [1, 1, 1, 1]   # Up, left, down, right
        
        while(i - scores[0] > 0 and original_grid[i - scores[0], j] < original_grid[i, j]):
            scores[0] += 1
        while(j - scores[1] > 0 and original_grid[i, j - scores[1]] < original_grid[i, j]):
            scores[1] += 1
        while(i + scores[2] < len(original_grid) - 1 and original_grid[i + scores[2], j] < original_grid[i, j]):
            scores[2] += 1
        while(j + scores[3] < len(original_grid) - 1 and original_grid[i, j + scores[3]] < original_grid[i, j]):
            scores[3] += 1

        if(scores[0] * scores[1] * scores[2] * scores[3] > best_score):
            best_score = scores[0] * scores[1] * scores[2] * scores[3]

    print(best_score)
# End Part 2