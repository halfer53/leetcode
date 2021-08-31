

int countSquares(int** matrix, int matrixSize, int* matrixColSize){
    int ret = 0;
    for (int i = 0; i < matrixSize; i++){
        for (int j = 0; j < *matrixColSize; j++){
            if(i == 0){
                ret += matrix[i][j];
            }else if(j == 0){
                ret += matrix[i][j];
            }else if(matrix[i][j] == 1){
                int min2 = matrix[i-1][j] < matrix[i][j-1] ? matrix[i-1][j] : matrix[i][j-1];
                int min = matrix[i-1][j-1] < min2 ? matrix[i-1][j-1] : min2;
                matrix[i][j] = min + 1;
                ret += (min + 1);
            }
        }
    }
    return ret;
}