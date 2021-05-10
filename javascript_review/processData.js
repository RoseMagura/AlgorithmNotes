const processData = input => {
    let evenArr = [];
    let oddArr = [];
    for (let i in input) {
        if (i % 2 === 0) {
            evenArr.push(input[i]);
        } else {
            oddArr.push(input[i]);
        }
    }
    console.log(evenArr.join(''), oddArr.join(''));
}

processData('adbecf');
processData('Hacker');
processData('Rank');