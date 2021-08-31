

int dfs(int **grid, int m, int n, int i, int j){
    if (i >= m)
        return j;
    if (!(0 <= j && j < n))
        return -1;
    if (grid[i][j] == 1 && j < n - 1 && grid[i][j+1] == 1)
        return dfs(grid, m, n, i+1, j+1);
    if (grid[i][j] == -1 && j > 0 && grid[i][j-1] == -1)
        return dfs(grid, m, n, i+1, j-1);
    return -1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findBall(int** grid, int gridSize, int* gridColSize, int* returnSize){
    int *ret = malloc(sizeof(int) * (*gridColSize));
    for(int i = 0; i < *gridColSize; i++){
        ret[i] = dfs(grid, gridSize, *gridColSize, 0, i);
    }
    *returnSize = *gridColSize;
    return ret;
}