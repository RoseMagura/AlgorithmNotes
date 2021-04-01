// const truncateString = (str, num) => {
//     return str.slice(0, num) + '...';
//   }
  
// console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8));
const findElement = (arr, func) => {
    return arr.filter(func)[0];
};

// console.log(findElement([1, 2, 3, 4], num => num % 2 === 0));
console.log(findElement([1, 3, 5, 8, 9, 10], num => num % 2 === 0));
// console.log(findElement([1, 2, 3, 4], num => num % 2 === 0));
