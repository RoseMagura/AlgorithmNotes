const checkName = (name, expectedValue) => {
    const myRegex = /(Eleanor|Franklin)\s[A-Z]?.?\s?Roosevelt/;
    const result = myRegex.test(name);
    if (result === expectedValue) {
        return 'Pass';
    } else {
        return 'Fail';
    }
};

const answerOne = checkName('Franklin D. Roosevelt', true);
console.log('A1', answerOne);

const answerTwo = checkName('Eleanor Roosevelt', true);
console.log('A2', answerTwo);

const answerThree = checkName('Franklin Rosevelt', false);
console.log('A3', answerThree);

const answerFour = checkName('Frank Roosevelt', false);
console.log('A4', answerFour);

const repeatRegex = (numberPhrase) => {
    // Caret means that part will come at the beginning
    // lowercase 'd' is a global search for digits
    // \s is for space
    let reRegex = /^(\d+)\s\1\s\1$/; 
    let result = reRegex.test(numberPhrase);
    return result;
}

console.log(repeatRegex('42 42 42'));
console.log(repeatRegex('42 42 42 42'));
