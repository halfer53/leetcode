

int longestLine(int** mat, int matSize, int* matColSize){
    int n = *matColSize;
    int dp[matSize][n][4];
    int ret = 0;
    
    for (int i = 0; i < matSize; i++){
        for (int j = 0; j < *matColSize; j++){
            for(int k = 0; k < 4; k++){
                dp[i][j][k] = mat[i][j];
            }
            if(mat[i][j]){
                if (i)
                    dp[i][j][0] = dp[i-1][j][0] + 1;
                if (j)
                    dp[i][j][1] = dp[i][j-1][1] + 1;
                if (i && j)
                    dp[i][j][2] = dp[i-1][j-1][2] + 1;
                if (i && j < *matColSize - 1)
                    dp[i][j][3] = dp[i-1][j+1][3] + 1;
                for(int k = 0; k < 4; k++){
                    ret = fmax(ret, dp[i][j][k]);
                }
            }
        }
    }
    return ret;
}