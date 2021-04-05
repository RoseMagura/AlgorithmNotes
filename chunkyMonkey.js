const chunkArrayInGroups = (arr, size) => {
    let newArr = [];
    let subArr = [];
    for(let i = 0; i < arr.length ;i++){
        if(subArr.length < size ){
            subArr.push(arr[i]);
        } else {
            newArr.push(subArr);
            // reset 
            subArr = [];
            subArr.push(arr[i]);
        }
    }
    newArr.push(subArr);
    return newArr;
}

// should return [['a', 'b'], ['c', 'd']]
console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2)); 
// should return [[0, 1, 2], [3, 4, 5]]
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3));
// should return [[0, 1], [2, 3], [4, 5]]
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2));
// should return [[0, 1, 2, 3], [4, 5]]
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4));
// should return [[0, 1, 2], [3, 4, 5], [6]]
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3));
// should return [[0, 1, 2, 3], [4, 5, 6, 7], [8]]
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4));
// should return [[0, 1], [2, 3], [4, 5], [6, 7], [8]]
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2));