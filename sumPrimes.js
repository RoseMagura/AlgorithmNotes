const sumPrimes = (num) => {
    let sum = 0;
    if(num <= 0) {
        return 'Error: Not valid input';
    }
    
    while(num > 1) {
        console.log(num);
        // check if number is prime
        let divisor = 2;
        while (divisor < num){
            // console.log(divisor, num);
            if(num % divisor === 0) {
                // console.log('not prime');
                break;
            }
            divisor++;
        }
        // console.log(num, 'divisor', divisor);
        if(divisor >= num) {
            // console.log(num, 'is prime');
            sum += num;
        }
        num--;
    }
    return sum;
}

console.log(sumPrimes(10));
console.log(sumPrimes(977));
// sumPrimes(10);