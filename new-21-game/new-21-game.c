

double new21Game(int n, int k, int maxPts){
    double ret = 0.0, tsum = 1.0;
    double dp[n+1];
    if (k == 0 || n >= (k + maxPts))
        return 1.0;
    memset(dp, 0, sizeof(double) * (n+1));
    dp[0] = 1.0;
    for(int i = 1; i <= n; i++){
        dp[i] = tsum / maxPts;
        if(i < k)
            tsum += dp[i];
        else
            ret += dp[i];
        if (i >= maxPts)
            tsum -= dp[i - maxPts];
    }
    return ret; 
    
}