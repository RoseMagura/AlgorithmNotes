const arr = [2, 4, 5, 1, 7, 5, 2, 1];
// Only change code below this line
arr.splice(0, 2);
arr.splice(1, 2);
arr.splice(2, 2);
// Only change code above this line
// console.log(arr);

function filteredArray(arr, elem) {
    let newArr = [];
    // Only change code below this line
    for(let i = 0; i < arr.length; i++) {
       arr[i].indexOf(elem) === -1 && newArr.push(arr[i]);
    }
    // Only change code above this line
    return newArr;
  }
  
//   console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3));
console.log(filteredArray([[10, 8, 3], [14, 6, 23], [3, 18, 6]], 18));