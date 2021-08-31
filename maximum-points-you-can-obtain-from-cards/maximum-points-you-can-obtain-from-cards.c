int maxScore(int* cardPoints, int cardPointsSize, int k){
    int n = cardPointsSize;
    int prefix[n], suffix[n];
    int ret = 0;
    prefix[0] = cardPoints[0];
    suffix[n-1] = cardPoints[n-1];
    for (int i = 1; i < n; i++){
        prefix[i] = cardPoints[i] + prefix[i-1];
    }
    for (int i = n - 2; i >= 0; i--){
        suffix[i] = cardPoints[i] + suffix[i+1];
    }
    int suffix_i = n - 1;
    ret = prefix[k-1] > suffix[n - k] ? prefix[k-1] : suffix[n-k];
    for (int i = 0; i < k; i++){
        int j = n - k + 1 + i;
        int sval = j >= n ? 0 : suffix[j];
        int val = prefix[i] + sval;
        ret = val > ret ? val : ret;
    }
    return ret;
}