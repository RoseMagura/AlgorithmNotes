const assert = require('assert');

const getIndexToIns = (arr, num) => {
    if(arr.length === 0){ 
        return 0;
    }
    const sortedArr = arr.sort((a, b) => a > b);
    for(let i = 0; i < arr.length; i++){
        if(sortedArr[i] === num){
            return i;
        }
        else if(sortedArr[i] < num && sortedArr[i + 1] >= num){
            return i + 1;
        }
    }
    return arr.length;
}

assert(getIndexToIns([40, 60], 50) === 1);
console.log(getIndexToIns([2, 5, 10], 15) === 3 ? 'Pass' : 'Fail');
console.log(getIndexToIns([3, 10, 5], 3) === 0 ? 'Pass' : 'Fail');
assert(getIndexToIns([5, 3, 20, 3], 5) === 2 ? 'Pass' : 'Fail'); 
console.log(getIndexToIns([], 1) === 0 ? 'Pass' : 'Fail');
console.log(getIndexToIns([10, 20, 30, 40, 50], 30) === 2 ? 'Pass' : 'Fail');