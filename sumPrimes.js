const sumPrimes = (num) => {
    let sum = 0;
    if(num <= 0) {
        return 'Error: Not valid input';
    }
    
    while(num > 1) {
        // check if number is prime
        let divisor = 2;
        while (divisor < num){
            if(num % divisor === 0) {
                break;
            }
            divisor++;
        }
        if(divisor >= num) {
            sum += num;
        }
        num--;
    }
    return sum;
}

console.log(sumPrimes(10));
console.log(sumPrimes(977));