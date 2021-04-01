const repeatStringNumTimes = (str, num) => {
    let newString = '';
    if (num <= 0) {
        return '';
    }
    while (num > 0) {
        num--;
        newString += str;
    }
    return newString;
}

const test = (input, output) => {
    input === output ? console.log('Pass') : console.log('Fail');
}

test(repeatStringNumTimes("abc", 3), 'abcabcabc');
test(repeatStringNumTimes('*', 3), '***');
test(repeatStringNumTimes('abc', 4), 'abcabcabcabc');
test(repeatStringNumTimes('abc', 0), '');
test(repeatStringNumTimes('abc', 1), 'abc');
test(repeatStringNumTimes('abc', -2), '');
test(repeatStringNumTimes('*', 8), '********');