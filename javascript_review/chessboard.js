/**
 * @param {string} coordinates
 * @return {boolean}
 */
const squareIsWhite = coordinates => {
    const startsOnBlack = new Set(['a', 'c', 'e', 'g']);
    const odd = parseInt(coordinates[1]) % 2 !== 0;
    if(startsOnBlack.has(coordinates[0])){
        if(odd){
            return false;
        } else {
            return true; 
        }
    } else {
        if(odd){
            return true;
        } else {
            return false; 
        }
    }
};

const testOne = squareIsWhite('a1'); // false
console.log(testOne);
const testTwo = squareIsWhite('h3'); // true
console.log(testTwo);
const testThree = squareIsWhite('c7'); // false
console.log(testThree);
const testFour = squareIsWhite('g8'); // true
console.log(testFour);
const testFive = squareIsWhite('b6'); // false
console.log(testFive);
const testSix = squareIsWhite('d3'); // true
console.log(testSix);

// complexity is linear