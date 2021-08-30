


typedef struct {
    int park[4];
} ParkingSystem;


ParkingSystem* parkingSystemCreate(int big, int medium, int small) {
    ParkingSystem* ps = malloc(sizeof(ParkingSystem));
    ps->park[1] = big;
    ps->park[2] = medium;
    ps->park[3] = small;
    return ps;
}

bool parkingSystemAddCar(ParkingSystem* obj, int carType) {
    if (obj->park[carType] < 1){
        return false;
    }
    obj->park[carType] -= 1;
    return true;
}

void parkingSystemFree(ParkingSystem* obj) {
    free(obj);
}

/**
 * Your ParkingSystem struct will be instantiated and called as such:
 * ParkingSystem* obj = parkingSystemCreate(big, medium, small);
 * bool param_1 = parkingSystemAddCar(obj, carType);
 
 * parkingSystemFree(obj);
*/