const fearNotLetter = (str) => {
    for(let index in str){
        console.log(str[index]);
        if(str.charCodeAt(index) - str.charCodeAt(index - 1) > 1){
            return String.fromCharCode(str.charCodeAt(index - 1) + 1);
        }
    }
    return;
}

console.log(fearNotLetter('abcde'));