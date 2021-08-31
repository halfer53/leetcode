

char * getHint(char * secret, char * guess){
    char *ret = malloc(sizeof(char) * 10);
    int n = strlen(secret);
    int hash[10];
    int bull = 0, cows = 0;
    memset(hash, 0, sizeof(int) * 10);
    for (int i = 0; i < n; i++){
        hash[(secret[i] - '0')]++;
    }
    for (int i = 0; i < n; i++){
        int sval = secret[i] - '0';
        int gval = guess[i] - '0';
        if (sval == gval){
            bull++;
            hash[sval]--;
            secret[i] = '\0';
        }
    }
    for (int i = 0; i < n; i++){
        int gval = guess[i] - '0';
        if(secret[i] && hash[gval] > 0){
            cows++;
            hash[gval]--;
        }
    }
    snprintf(ret, 10, "%dA%dB", bull, cows);
    return ret;
}