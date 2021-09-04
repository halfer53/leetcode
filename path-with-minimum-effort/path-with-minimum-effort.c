int dfs(int **heights, int m, int n, int visited[m][n], int i, int j, int k, int prev){
    if (i < 0 || i >= m || j < 0 || j >= n)
        return 0;
    if (prev && abs(heights[i][j] - prev) > k)
        return 0;
    if (visited[i][j])
        return 0;
    if (i == m - 1 && j == n - 1)
        return 1;
    visited[i][j] = 1;
    int r1 = dfs(heights, m, n, visited, i-1, j, k, heights[i][j]);
    int r2 = dfs(heights, m, n, visited, i+1, j, k, heights[i][j]);
    int r3 = dfs(heights, m, n, visited, i, j-1, k, heights[i][j]);
    int r4 = dfs(heights, m, n, visited, i, j+1, k, heights[i][j]);
    return r1 + r2 + r3 + r4;
}

int minimumEffortPath(int** heights, int heightsSize, int* heightsColSize){
    int m = heightsSize, n = *heightsColSize;
    int left = 0, right = pow(10, 6);
    int visited[m][n];
    
    while (left <= right){
        int mid = left + (right - left) / 2;
        memset(visited, 0, sizeof(visited));
        int val = dfs(heights, m, n, visited, 0, 0, mid, 0);
        if (val){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }
    return left;
}