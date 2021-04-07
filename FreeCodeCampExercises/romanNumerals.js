const convertToRoman = num => {
    let final = '';
    const thousands = Math.floor(num / 1000);
    const fiveHundreds = Math.floor(num / 500);
    const hundreds = Math.floor(num / 100);
    const fifties = Math.floor(num / 50);
    const tens = Math.floor(num / 10);

    const remainder = num - tens * 10; // unfinished
    console.log(remainder);

    if(tens > 0 && tens < 4){
        final += 'X'.repeat(tens);
    } else if(tens > 5) {
        final += 'L' + 'X'.repeat(tens - 5);
    } else {
        final += 'L';
    }

    if(remainder > 0 && remainder < 4){
        final += 'I'.repeat(remainder);
    } else if (remainder > 5){
        final += 'V' + 'I'.repeat(remainder - 5);
    } else {
        final += 'V';
    }
    // console.log(thousands, fiveHundreds, hundreds, fifties, tens);
    console.log(final);
    return final;
}

// console.assert(convertToRoman(1) === 'I');
console.log(convertToRoman(1));
// convertToRoman(36);
// convertToRoman(60);
// convertToRoman(50);
