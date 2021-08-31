

int minEatingSpeed(int* piles, int pilesSize, int h){
    int tmax = 0, left = 1, right = 0;
    
    for(int i = 0; i < pilesSize; i++){
        tmax = fmax(tmax, piles[i]);
    }
    right = tmax;
    while (left <= right){
        int mid = (left + right) / 2;
        bool canfinish = false;
        int hours = 0;
        for(int i = 0; i < pilesSize; i++){
            // hours += (piles[i] / mid) + (piles[i] % mid == 0 ? 0 : 1);
            hours += ceil((double)(piles[i]) / (double)mid);
        }
        if (hours <= h){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }
    return left;
}