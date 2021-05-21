/*
 * Complete the 'rotLeft' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER d
 */

const rotLeft = (a, d) => {
    // Write your code here
    while(d > 0){
        const first = a.shift();
        a.push(first);
        d--;
    }
    return a;
}

rotLeft([1, 2, 3, 4, 5], 4);