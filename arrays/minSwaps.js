const minSwaps = arr => {
    let swaps = 0;
    const indices = {};
    const values = {};
    arr.forEach(el => {
        indices[arr.indexOf(el) + 1] = el;
        values[el] = arr.indexOf(el) + 1;
    });

    for (let i = 1; i <= Object.keys(indices).length; i++) {
        if (indices[i] !== i) {
            const firstValue = indices[i];
            const secondValue = values[firstValue];

            const firstIndex = i;
            const secondIndex = values[i];

            indices[firstIndex] = secondValue;
            indices[secondIndex] = firstValue;
            values[firstValue] = secondIndex;
            values[secondValue] = firstIndex;
            swaps++;
        }
    }
    console.log(swaps);
    return swaps;
}

// solution found on discussion board
const fasterMinSwaps = arr => {
    const rotArr = Object.values(Object.assign({}, arr));
    let minVal;
    // var maxVal = Math.max(...rotArr);
    let minValInd;
    let currentVal;
    let swapCount = 0;

    for (let i = 0; i < rotArr.length; i++) {
        // get minimum values
        minVal = Math.min(...arr);

        // if value at current index is the lowest, continue without swapping 
        if (minVal === rotArr[i]) {
            arr.shift();
            continue;
        }

        // otherwise, find the index of lowest value
        minValInd = rotArr.indexOf(minVal);

        currentVal = rotArr[i];
        // swap lowest value and current value here
        rotArr[i] = rotArr[minValInd];
        rotArr[minValInd] = currentVal;

        arr = Object.values(Object.assign({}, rotArr.slice(i)));
        arr.shift();

        // find next min before next iteration
        minVal = Math.min(...arr);
        swapCount++;
    }
    return swapCount;
}

minSwaps([7, 1, 3, 2, 4, 5, 6]); // should return 5
// minSwaps([4, 3, 1, 2]); // should return 3
// minSwaps([2, 3, 4, 1, 5]); // should return 3
// minSwaps([1, 3, 5, 2, 4, 6, 7]); // should return 3