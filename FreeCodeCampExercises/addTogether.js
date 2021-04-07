function addTogether() {
    const args = Array.from(arguments);

    const invalidInput = args.some(el => typeof (el) !== 'number');
    if (invalidInput) {
        return;
    }

    if (args.length === 1) {
        return function addSecond(second) {
            return args[0] + second;
        }
    }

    return args.reduce((sum, val) => sum += val);
}

console.log(addTogether(2, 3)); // should return 5
const sumTwoAnd = addTogether(2);
const combined = sumTwoAnd(3);
console.log(combined); // should return 5

console.log(addTogether("http://bit.ly/IqT6zt")); // should return undefined
console.log(addTogether(2, '3')); // should return undefined
console.log(addTogether(2)[3]); // should return undefined
