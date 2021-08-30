
bool ispredecessor(char* w1, char* w2){
    bool skipped = false;
    int l1 = strlen(w1), l2 = strlen(w2);
    if (l2 - l1 != 1){
        return false;
    }
    while (*w1 && *w2){
        if(*w1 != *w2){
            if(skipped)
                return false;
            skipped = true;
            w2++;
        }else{
            w1++;
            w2++;
        }
    }
    return true;
}

int cmp(const void* a, const void* b){
    return strlen( *(const char**)a) - strlen(*(const char**)b );
}

int longestStrChain(char ** words, int wordsSize){
    int dp[wordsSize];
    int ret = 1;
    memset(dp, 0, sizeof(int) * wordsSize);
    for(int i = 0; i < wordsSize; i++){
        dp[i] = 1;
    }
    qsort(words, wordsSize, sizeof(char*), cmp);
    for(int i = i; i < wordsSize; i++){
        for(int j = i+1; j < wordsSize; j++){
            bool ispre = ispredecessor(words[i], words[j]);
            if(ispre){
                int val = dp[i] + 1;
                dp[j] = val > dp[j] ? val : dp[j];
                ret = dp[j] > ret ? dp[j] : ret;
                // printf("%d %d %d %d\n", j, i, val, dp[i]);
            }
        }
    }
    return ret;
}