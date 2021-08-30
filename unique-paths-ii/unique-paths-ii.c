

int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    int m = obstacleGridSize;
    int n = *obstacleGridColSize;
    int** dp = obstacleGrid;
    int i, j, set = 1;
    if(dp[0][0] == 1)
        return 0;
    for (i = 0; i < m; i++){
        if(dp[i][0] == 1){
            set = 0;
        }
        dp[i][0] = set;
    }
    set = 1;
    for (i = 1; i < n; i++){
        if(dp[0][i] == 1){
            set = 0;
        }
        dp[0][i] = set;
    }
    // printf("%d %d\n", m, n);
    // for (i = 0; i < m; i++){
    //     for(j = 0; j < n; j++){
    //         printf("%d ", dp[i][j]);
    //     }
    //     printf("\n");
    // }
    for (i = 1; i < m; i++){
        for(j = 1; j < n; j++){
            if(dp[i][j] == 1){
                dp[i][j] = 0;
            }else{
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    return dp[m-1][n-1];
}