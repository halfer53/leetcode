
int cmp(const void*a, const void* b){
    int *pa = (*(int**)a), *pb = (*(int**)b);
    if (pa[0] == pb[0])
        return pa[1] - pb[1];
    else
        return pa[0] - pb[0];
}

double dist(int* p1, int* p2) {
    return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0]);
}

bool validSquare(int* p1, int p1Size, int* p2, int p2Size, int* p3, int p3Size, int* p4, int p4Size){
    int* p[4] = {p1, p2, p3, p4};
    qsort(p, 4, sizeof(int *), cmp);
    return dist(p[0], p[1]) != 0 && dist(p[0], p[1]) == dist(p[1], p[3]) && dist(p[1], p[3]) == dist(p[3], p[2]) && dist(p[3], p[2]) == dist(p[2], p[0])   && dist(p[0],p[3])==dist(p[1],p[2]);
}