int dfs(int **grid, int m, int n, int i, int j){
    if (i < 0 || i >= m || j < 0 || j >= n)
        return 0;
    if (grid[i][j] == 1)
        return 1;
    grid[i][j] = 1;
    int r1 = dfs(grid, m, n, i+1, j);
    int r2 = dfs(grid, m, n, i, j+1);
    int r3 = dfs(grid, m, n, i-1, j);
    int r4 = dfs(grid, m, n, i, j-1);
    return r1 & r2 & r3 & r4;
}

int closedIsland(int** grid, int gridSize, int* gridColSize){
    int m = gridSize, n = *gridColSize;
    int ret = 0;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (grid[i][j] == 0){
                ret += dfs(grid, m, n, i, j);
            }
        }
    }
    return ret;
}