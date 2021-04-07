const myReplace = (str, before, after) => {
    const words = str.split(' ');
    for(let w in words){
        if(words[w] === before){
            console.log(words[w][0].toLowerCase() === words[w][0]);
            if(words[w][0].toLowerCase() !== words[w][0]) {
                console.log('word is uppercase');
                const capitalizedAfter = after[0].toUpperCase() + after.slice(1);
                words[w] = capitalizedAfter;
                break;
            }
            words[w] = after.toLowerCase();
        }
    }
    return words.join(' ');
  }
  
console.log(myReplace("A quick brown fox Jumped over the lazy dog", "Jumped", "leaped"));