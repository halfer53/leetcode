
int cmp(const void* a, const void* b){
    int *arr_a = *(int **)a;
    int *arr_b = *(int **)b;
    if (arr_a[0] == arr_b[0]){
        return arr_b[1] - arr_a[1]; 
    }
    return arr_a[0] - arr_b[0];
}

int numberOfWeakCharacters(int** properties, int propertiesSize, int* propertiesColSize){
    int ret = 0, maxright = 0;
    qsort(properties, propertiesSize, sizeof(int *), cmp);
    for (int i = propertiesSize - 1; i >= 0; i--){
        if (properties[i][1] < maxright)
            ret++;
        maxright = fmax(maxright, properties[i][1]);
    }
    return ret;
}