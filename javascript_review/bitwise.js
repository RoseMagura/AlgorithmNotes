const calculateBitwise = (n, k) => {
    let max = 0;
    let a = 1;
    let b = 2;
    while (a < n){
        while (b <= n) {
            if((a & b) < k && (a & b) > max){
                    max = a & b;
            }
            b++;
        }
        a++;
        b = a + 1; // reset
    }
    console.log(max);
    return max;
}

calculateBitwise(5, 2); // should return 1
calculateBitwise(8, 5); // should return 4
calculateBitwise(9, 2); // should return 1
calculateBitwise(8, 3); // should return 2