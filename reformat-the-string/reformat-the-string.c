
char * reformat(char * s){
    int n = strlen(s);
    int i = 0;
    int num = 0, letter = 0;
    char numlist[n], letterlist[n];
    char *p = s, *nend = numlist, *lend = letterlist, *m, *l;
    char *ret = malloc(sizeof(char) * n + 1);
    while(*p){
        if(isdigit(*p)){
            num += 1;
            *nend++ = *p;
        }else{
            letter += 1;
            *lend++ = *p;
        }
        p += 1;
    }
    if (abs(num - letter) > 1){
        return "";
    }
    m = num > letter ? numlist : letterlist;
    l = num > letter ? letterlist : numlist;
    for(i = 0; i < n; i++){
        if (i % 2 == 0 ){
            ret[i] = *m++;
        }else{
            ret[i] = *l++;
        }
    }
    ret[n] = '\0';
    return ret;
}