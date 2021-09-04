
int dfs(char **grid, int m, int n, int i, int j){
    if (i < 0 || i >= m || j < 0 || j >= n )
        return 1;
    if (grid[i][j] == '0')
        return 1;
    grid[i][j] = '0';
    int r1 = dfs(grid, m, n, i-1,j);
    int r2 = dfs(grid, m, n, i+1, j);
    int r3 = dfs(grid, m, n, i, j-1);
    int r4 = dfs(grid, m, n, i, j+1);
    return r1 && r2 && r3 && r4;
}

int numIslands(char** grid, int gridSize, int* gridColSize){
    int ret = 0;
    int m = gridSize, n = *gridColSize;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (grid[i][j] == '1'){
                int val = dfs(grid, m, n, i,j);
                ret += val;
            }
        }
    }
    return ret;
}