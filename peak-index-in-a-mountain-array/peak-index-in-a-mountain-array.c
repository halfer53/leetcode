

int peakIndexInMountainArray(int* arr, int arrSize){
    int left = 0, right = arrSize - 1;
    bool incr[arrSize], decr[arrSize];
    incr[0] = true;
    decr[arrSize-1] = true;
    for (int i = 1; i < arrSize; i++){
        if(arr[i-1] < arr[i]){
            incr[i] = incr[i-1] & true;
        }else{
            incr[i] = false;
        }
    }
    for (int i = arrSize - 2; i >= 0; i--){
        if(arr[i] > arr[i+1]){
            decr[i] = decr[i+1] & true;
        }else{
            decr[i] = false;
        }
    }
    for (int i = 1; i < arrSize - 1; i++){
        if (incr[i] && decr[i]){
            return i;
        }
    }
    return -1;
}