const factorialize = (num) => {
    if(num === 0 || num === 1){
        return 1;
    }
    let value = 1;
    while(num > 1) {
        value *= num;
        num--;
    }
    return value;
}

const test = (input, output) => {
    input === output ? console.log('Pass') : console.log('Fail');
}

test(factorialize(5), 120);
test(factorialize(10), 3628800);
test(factorialize(20), 2432902008176640000);
test(factorialize(0), 1);