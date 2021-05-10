/*
 * Complete the 'repeatedString' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. LONG_INTEGER n
 */

const repeatedString = (s, n) => {
    // Write your code here
    if(s.length === 1){
        return n;
    }
    let count = 0;
    const arr = s.split('');
    arr.map(char => char === 'a' && count++);
    const timesRepeated = n / s.length;
    return Math.ceil(count * timesRepeated);
}

const testOne = repeatedString('aba', 10);
console.log(testOne);