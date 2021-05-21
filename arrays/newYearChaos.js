/*
 * Complete the 'minimumBribes' function below.
 *
 * The function accepts INTEGER_ARRAY q as parameter.
 */

const minimumBribes = (q) => {
    // Write your code here
    let bribes = 0;
    let min = q.length;
    for (let index = q.length - 1; index >= 0; index--) {
        const diff = q[index] - index;
        if (diff > 3) {
            return 'Too chaotic';
        } 
        if (q[index] > index+1){
            bribes += (q[index]-(index+1));
        } else {
            if (min > q[index]) {
                min = q[index];
            } else if (q[index] !== min){
                bribes++;
            }
        }
    }
    console.log(bribes);
    return bribes;
}

// const testOne = minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]); // should print 1
// const testTwo = minimumBribes([4, 1, 2, 3]); // should print 'Too chaotic'
// const testThree = minimumBribes([2, 1, 5, 3, 4]); // should print 3
// const testFour = minimumBribes([2, 5, 1, 3, 4]); // should print 'Too chaotic'
// const testFive = minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]); // should print 'Too chaotic'
const testSix = minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]); // should print 7