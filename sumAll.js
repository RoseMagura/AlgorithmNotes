
const sumAll = (arr) => {
    let sum = 0;
    const sorted = arr.slice().sort((a, b) => a > b);
    let i = sorted[0];
    while (i <= sorted[1]){
      sum += i;
      i++;
    }
    return sum;
  }
  
  sumAll([4, 1]);
  sumAll([5, 10]);
  sumAll([10, 5]);