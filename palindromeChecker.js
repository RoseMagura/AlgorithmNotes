const palindromeChecker = (str) => {
    const specialChar = '~!@#$%^&*()_+/\\-:|?., ';
    let lettersAndNum = [];
    for(char of str) {
        if(!specialChar.includes(char)) {
            lettersAndNum.push(char.toLowerCase());
        }
    }
    // console.log(lettersAndNum);
    let start = 0;
    let end = lettersAndNum.length - 1;
    while(start < end) {
        if(lettersAndNum[start] !== lettersAndNum[end]){
            return false;
        };
        start++;
        end--;
    }
    return true;
}

const test = (input, output) => {
    console.log(input === output ? 'Pass' : 'Fail');
}

test(palindromeChecker('**ey?e_'), true);
test(palindromeChecker('eye'), true);
test(palindromeChecker('_eye'), true);
test(palindromeChecker('race car'), true);
test(palindromeChecker('not a palindrome'), false);
test(palindromeChecker('A man, a plan, a canal. Panama'), true);
test(palindromeChecker('never odd or even'), true);
test(palindromeChecker('nope'), false);
test(palindromeChecker('almostomla'), false);
test(palindromeChecker('My age is 0, 0 si ega ym.'), true);
test(palindromeChecker('1 eye for of 1 eye.'), false);
test(palindromeChecker('0_0 (: /-\ :) 0-0'), true);
test(palindromeChecker('five|\_/|four'), false);
