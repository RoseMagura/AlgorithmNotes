const dropElements = (arr, func) => {
    for (const element of arr) {
        if (func(element)) {
            return arr.slice(arr.indexOf(element));
        }
    }
    return [];
}

// const res = dropElements([1, 2, 3, 4], n => n >= 3);
// const res = dropElements([0, 1, 0, 1], n => n === 1);
const res = dropElements([1, 2, 3, 9, 2], n => n > 2);
// const res = dropElements([1, 2, 3, 4], n => n > 5);
console.log(res);