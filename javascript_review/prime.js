// O(n) complexity
const checkPrime = input => {
    if (input === 1) {
        console.log('Not prime');
        return;
    }

    let divisor = 2;
    while (divisor < input / 2) {
        if (input % divisor === 0) {
            console.log('Not prime');
            return;
        }
        divisor++;
    }
    console.log('Prime');
}

// Efficiency of O(n^(1/2))
const betterCheckPrime = n => {
    if (n === 1) {
        console.log('Not prime');
        return;
    } else if (n === 2) {
        console.log('Prime');
        return;
    }
    let divisor = 2;
    while (divisor < Math.sqrt(n)) {
        if (n % divisor === 0) {
            console.log('Not prime');
            return;
        }
        divisor++;
    }
    console.log('Prime');
}

const bestCheckPrime = num => {
    if (num === 2) {
        console.log('Prime');
        return;
    } else if (num === 1 || num % 2 === 0) {
        // One and even numbers greater than 2 are not prime
        console.log('Not prime');
        return;
    }

    // Only check odd numbers from 3 to square root of the number
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        if (n % i === 0) {
            console.log('Not prime');
            return;
        }
    }
    console.log('Prime');
}

checkPrime(5);
checkPrime(7);
checkPrime(12);
checkPrime(13);
checkPrime(14);
checkPrime(15);
