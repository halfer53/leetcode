

int numSplits(char * s){
    int n = strlen(s);
    int prefix[n], suffix[n];
    int hash[26];
    int ret = 0;
    memset(hash, 0, sizeof(int) * 26);
    prefix[0] = 1;
    hash[(s[0] - 'a')] = 1;
    for(int i = 1; i < n; i++){
        int val = prefix[i-1];
        if(hash[(s[i] - 'a')] == 0)
            val++;
        hash[(s[i] - 'a')]++;
        prefix[i] = val;
        
    }
    memset(hash, 0, sizeof(int) * 26);
    suffix[n-1] = 1;
    hash[(s[n-1] - 'a')] = 1;
    for(int i = n-2; i >= 0; i--){
        int val = suffix[i+1];
        if(hash[(s[i] - 'a')] == 0)
            val++;
        hash[(s[i] - 'a')]++;
        suffix[i] = val;
    }

    for(int i = 0; i < n-1; i++){
        if(prefix[i] == suffix[i+1]){
            
            ret++;
        }
            
    }
    return ret;
}