const makeAnagram = (a, b) => {
    let deletions = 0;
    for(let char of a){
        if(!b.includes(char)){
            deletions++;
        }
    }

    for(let letter of b){
        if(!a.includes(letter)){
            deletions++;
        }
    }
    console.log(deletions);
    return deletions;
}

makeAnagram('cde', 'abc');