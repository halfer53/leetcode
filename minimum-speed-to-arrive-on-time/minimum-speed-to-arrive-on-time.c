
int can_finish(int* dist, int n, int k, double hour){
    double curr = 0.0;
    for (int i = 0; i < n; i++){
        double val = (double)dist[i] / (double)k;
        curr += val;
        if (i < n - 1)
            curr = ceil(curr);
        // printf("%d %d %f %f %f\n", dist[i], k, val, curr, ceil(curr));
    }
    return curr <= hour;
}

int minSpeedOnTime(int* dist, int distSize, double hour){
    int left = 1, right = pow(10, 8);
    int ret = INT_MAX;
    while (left <= right){
        int mid = left + (right - left) / 2;
        int result = can_finish(dist, distSize, mid, hour);
        if (result){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }
    if (left >= pow(10, 8))
        return -1;
    return left;
}