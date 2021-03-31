const findLongestWordLength = (str) => {
    const arr = str.split(' ');
    arr.sort((a, b) => b.length > a.length);
    return arr[0].length;
}

const test = (input, output) => {
    input === output ? console.log('Pass') : console.log('Fail');
}

test(findLongestWordLength('The quick brown fox jumped over the lazy dog'), 6);
test(findLongestWordLength("May the force be with you"), 5);
test(findLongestWordLength("Google do a barrel roll"), 6);
test(findLongestWordLength("What is the average airspeed velocity of an unladen swallow"), 8);
test(findLongestWordLength("What if we try a super-long word such as otorhinolaryngology"), 19);