


typedef struct {
    int* encoding;
    int size;
    int i;
} RLEIterator;


RLEIterator* rLEIteratorCreate(int* encoding, int encodingSize) {
    RLEIterator* ret = malloc(sizeof(RLEIterator));
    ret->encoding = encoding;
    ret->size = encodingSize;
    ret->i = 0;
    return ret;
}

int rLEIteratorNext(RLEIterator* obj, int n) {
    while (obj->i < obj->size && n > obj->encoding[obj->i]){
        n -= obj->encoding[obj->i];
        obj->i += 2;
    }
    if (obj->i >= obj->size){
        return -1;
    }
    obj->encoding[obj->i] -= n;
    return obj->encoding[(obj->i + 1)];
}

void rLEIteratorFree(RLEIterator* obj) {
    free(obj);
}

/**
 * Your RLEIterator struct will be instantiated and called as such:
 * RLEIterator* obj = rLEIteratorCreate(encoding, encodingSize);
 * int param_1 = rLEIteratorNext(obj, n);
 
 * rLEIteratorFree(obj);
*/