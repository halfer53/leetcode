

int maxDistToClosest(int* seats, int seatsSize){
    int n = seatsSize;
    int ret = 0, idx = 0;
    int prefix[n], suffix[n];
    memset(prefix, 1, sizeof(prefix));
    memset(suffix, 1, sizeof(suffix));
    for (int i = 0; i < n; i++){
        if (seats[i] == 1){
            prefix[i] = 0;
        }else if (i){
            prefix[i] = prefix[i-1] + 1;
        }
    }
    
    for (int i = n-1; i >= 0; i--){
        if (seats[i] == 1){
            suffix[i] = 0;
        }else if (i < n - 1){
            suffix[i] = suffix[i+1] + 1;
        }
    }
    
    for (int i = 0; i < n; i++){
        int val = fmin(prefix[i], suffix[i]);
        ret = fmax(ret, val);
    }
    return ret;
}