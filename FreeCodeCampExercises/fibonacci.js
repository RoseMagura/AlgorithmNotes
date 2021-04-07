const sumFibs = (num) => {
    let fib = 1; // first Fibonacci number
    let prevFib = 0;
    let placeholder = prevFib;
    let sum = 0;

    if(num === 1){
        sum += fib;
        return sum;
    }

    prevFib = 1; // fib stays at one and prevFib is increased to one 
                // because Fibonacci sequence begins with 1, 1 
    sum += fib; // sum is 2
    while(fib <= num) {
        if(fib % 2 !== 0) {
            sum += fib;
        }
        placeholder = fib;
        fib += prevFib;
        prevFib = placeholder;

    }
    return sum;
}

sumFibs(1); // should return 1
sumFibs(4); // should return 5
sumFibs(1000); // should return 1785
sumFibs(75024); // should return 60696
sumFibs(75025); // should return 135721
sumFibs(4000000); // should return 4613732