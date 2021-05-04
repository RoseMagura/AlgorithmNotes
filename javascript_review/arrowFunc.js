const modifyArray = nums => nums.map(num => num % 2 === 0 ? num * 2 : num * 3);


const output = modifyArray([1, 2, 3, 4, 5]);
console.log(output);