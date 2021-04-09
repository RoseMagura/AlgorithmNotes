const assert = require('assert');

const convertToRoman = num => {
    let final = '';
    let current = num;
    const thousands = Math.floor(current / 1000);
    current -= thousands * 1000;
    const fiveHundreds = Math.floor(current / 500);
    current -= fiveHundreds * 500;
    const hundreds = Math.floor(current / 100);
    current -= hundreds * 100;
    const fifties = Math.floor(current / 50);
    current -= fifties * 50;
    const tens = Math.floor(current / 10);
    current -= tens * 10;

    const remainder = current;
    console.log(thousands, fiveHundreds, hundreds, fifties, tens, remainder);

    // thousands
    if(thousands > 0 && thousands < 4){
        final += 'M'.repeat(thousands);
    } else if(thousands > 5){
        final += 'V' + 'M'.repeat(thousands - 5); // note that this is the one that represents five thousand
    } else if (thousands === 5){
        final += 'V';
    } else if (thousands === 4){
        final += 'IV';
    }

    // five hundreds
    if(fiveHundreds > 0 && fiveHundreds < 4){
        final += 'D'.repeat(fiveHundreds);
    } 
    // else if (fiveHundreds > 5) {
    //     return final += 'D' + 'C'.repeat(fiveHundreds - 5);
    // } else if(fiveHundreds === 5)

    // hundreds
    if(hundreds > 0 && hundreds < 4){
        final += 'C'.repeat(hundreds);
    } else if (hundreds === 4) {
        final += 'CD';
    }

    // fifties
    if(fifties > 5){
        final += 'L' + 'X'.repeat(fifties - 5);
    } else if (fifties === 1) {
        final += 'L';
    }

    // tens
    if(tens > 0 && tens < 4){
        final += 'X'.repeat(tens);
    } else if(tens > 5) {
        final += 'L' + 'X'.repeat(tens - 5);
    } else if (tens === 5) {
        final += 'L';
    } else if (tens === 4) {
        final += 'XL'
    }

    // ones
    if(remainder > 0 && remainder < 4){
        final += 'I'.repeat(remainder);
    } else if (remainder > 5 && remainder < 9){
        final += 'V' + 'I'.repeat(remainder - 5);
    } else if (remainder === 5) {
        final += 'V';
    } else if (remainder === 4) {
        final += 'IV';
    } else if (remainder === 9) {
        final += 'IX'
    }
    // console.log(thousands, fiveHundreds, hundreds, fifties, tens);
    console.log(final);
    return final;
}

// assert(convertToRoman(1) === 'I', 'Fail');
// assert(convertToRoman(2) === 'II', 'Fail');
// assert(convertToRoman(3) === 'III', 'Fail');
// assert(convertToRoman(4) === 'IV', 'Fail');
// assert(convertToRoman(5) === 'V', 'Fail');
// assert(convertToRoman(6) === 'VI', 'Fail');
// assert(convertToRoman(7) === 'VII', 'Fail');
// assert(convertToRoman(8) === 'VIII', 'Fail');
// assert(convertToRoman(9) === 'IX', 'Fail');
// assert(convertToRoman(10) === 'X', 'Fail');


// convertToRoman(44);
// convertToRoman(45);

convertToRoman(97); // should return XCVII
// convertToRoman(99); // should return XCIX

// convertToRoman(400);  // should return CD
// convertToRoman(500);  // should return D
// convertToRoman(501);  // should return DI
// convertToRoman(649);  // should return DCXLIX
// convertToRoman(798);  // should return DCCXCVIII
// convertToRoman(891);  // should return DCCCXCI 
// convertToRoman(1000); // should return M
// convertToRoman(1004); // should return MIV   
// convertToRoman(1006); // should return MVI
// convertToRoman(1023); // should return MXXIII   
// convertToRoman(2014); // should return MMXIV
// convertToRoman(3999); // should return MMMCMXCIX







