function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match ALL occurrences of numbers in a string.
     */
    
    const re = new RegExp('\\d+', 'g');
    /*
     * Do not remove the return statement
     */
    return re;
}


function main() {
    const re = regexVar();
    // const s = readLine();
    const s = '102';
    
    const r = s.match(re);
    
    for (const e of r) {
        console.log('digit', e);
    }
}

main();