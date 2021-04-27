const assert = require('assert');

const convertToRoman = num => {
    let final = '';
    const decimalValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const romanNumerals = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I"
      ];
    
    for(let i=0; i < decimalValues.length; i++) {
        while(decimalValues[i] <= num){
            final += romanNumerals[i];
            num -= decimalValues[i];
        }
    }
    return final;
}

assert(convertToRoman(1) === 'I', 'Fail');
assert(convertToRoman(2) === 'II', 'Fail');
assert(convertToRoman(3) === 'III', 'Fail');
assert(convertToRoman(4) === 'IV', 'Fail');
assert(convertToRoman(5) === 'V', 'Fail');
assert(convertToRoman(6) === 'VI', 'Fail');
assert(convertToRoman(7) === 'VII', 'Fail');
assert(convertToRoman(8) === 'VIII', 'Fail');
assert(convertToRoman(9) === 'IX', 'Fail');
assert(convertToRoman(10) === 'X', 'Fail');


convertToRoman(44);
convertToRoman(45);

convertToRoman(97); // should return XCVII
convertToRoman(99); // should return XCIX

convertToRoman(400);  // should return CD
convertToRoman(500);  // should return D
convertToRoman(501);  // should return DI
convertToRoman(649);  // should return DCXLIX
convertToRoman(798);  // should return DCCXCVIII
convertToRoman(891);  // should return DCCCXCI 
convertToRoman(1000); // should return M
convertToRoman(1004); // should return MIV   
convertToRoman(1006); // should return MVI
convertToRoman(1023); // should return MXXIII   
convertToRoman(2014); // should return MMXIV
convertToRoman(3999); // should return MMMCMXCIX







