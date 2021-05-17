/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

const hourglassSum = (arr) => {
    // Write your code here
    let maxSum = -63;
    let sum = 0;
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] // first row
                + arr[i + 1][j + 1] // middle row of hourglass
                + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]; // last row of hourglass
            if (sum > maxSum) {
                maxSum = sum;
            }
            sum = 0; // reset
        }
    }
    return maxSum;
}

hourglassSum(
    [[1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]
); // should return 19

hourglassSum(
    [[-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]]
); // should return 28