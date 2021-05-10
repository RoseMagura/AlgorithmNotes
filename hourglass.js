/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

const hourglassSum = (arr) => {
    // Write your code here
    let sums = [];
    for (let x = 0; x < 4; x ++) {
        for (let y = 0; y < 4; y++) {
            console.log(arr[x][y]);
            // sums.push();
        }
    }

}

hourglassSum(
    [[-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]]
);