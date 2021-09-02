

long long maxPoints(int** points, int pointsSize, int* pointsColSize){
    int m = pointsSize, n = *pointsColSize;
    long long dp[m][n];
    memset(dp, 0, sizeof(dp));
    long long ret = 0;
    for(int j= 0; j < n; j++){
        dp[0][j] = points[0][j];
    }
    for(int i = 1; i < m; i++){
        long long leftdp[n], rightdp[n];
        memset(leftdp, 0, sizeof(leftdp));
        memset(rightdp, 0, sizeof(rightdp));
        leftdp[0] = dp[i-1][0];
        // Assuming left items are bigger, We need to subtract (j - k) = -j + k
        for (int k = 1; k < n; k++){
            leftdp[k] = fmax(leftdp[k-1], dp[i-1][k] + k);
        }
        rightdp[n-1] = dp[i-1][n-1] - n + 1;
        for (int k = n-2; k >= 0; k--){
            rightdp[k] = fmax(rightdp[k+1], dp[i-1][k] - k);
        }
        for(int j = 0; j < n; j++){
            dp[i][j] = fmax(leftdp[j] - j, rightdp[j] + j) + points[i][j];
        }
    }
    for(int j = 0; j < n; j++){
        ret = fmax(ret, dp[m-1][j]);
    }
    return ret;
}