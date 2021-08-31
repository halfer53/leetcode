struct car{
    int pos;
    double time;
};
int cmp(const void* a, const void *b){
    return ((struct car*)a)->pos - ((struct car*)b)->pos;
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize){
    struct car cars[positionSize];
    int ret = 1;
    double curr = 0;
    for(int i = 0; i < positionSize; i++){
        cars[i].pos = position[i];
        cars[i].time = (double)(target - position[i]) / (double)speed[i];
    }
    qsort(cars, positionSize, sizeof(struct car), cmp);
    curr = cars[positionSize - 1].time;
    for(int i = positionSize - 2; i >= 0; i--){
        // printf("%f %f\n", cars[i].time, curr);
        if (cars[i].time > curr){
            curr = cars[i].time;
            ret++;
        }
    }
    return ret;
}