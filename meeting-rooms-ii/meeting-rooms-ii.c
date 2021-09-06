
int cmp(const void *a, const void *b){
    return (*(int *)a) - (*(int *)b);
}

int minMeetingRooms(int** intervals, int intervalsSize, int* intervalsColSize){
    int i = 0, usedrooms = 0;
    int n = intervalsSize;
    int start[n], end[n];
    for (int i = 0; i < intervalsSize; i++){
        start[i] = intervals[i][0];
        end[i] = intervals[i][1];
    }
    qsort(start, n, sizeof(int), cmp);
    qsort(end, n, sizeof(int), cmp);
    int i_start = 0, i_end = 0;
    while (i_start < n && i_end < n){
        if (start[i_start] >= end[i_end]){
            usedrooms--;
            i_end++;
        }
        usedrooms++;
        i_start++;
    }
    
    return usedrooms;
}