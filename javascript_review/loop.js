/* 
Task (From HackerRank)

First, print each vowel in s on a new line. 
The English vowels are a, e, i, o, and u, and each vowel must be printed 
in the same order as it appeared in s

Second, print each consonant (i.e., non-vowel) in
on a new line in the same order as it appeared in s 
*/

const vowelsAndConsonants = (s) => {
    const vowelRef = ['a', 'e', 'i', 'o', 'u'];

    let consonants = [];

    for(index in s){
        if(vowelRef.includes(s[index])){
            console.log(s[index]);
        } else {
            consonants.push(s[index]);
        }
    }

    consonants.forEach(char => console.log(char));
}

vowelsAndConsonants('javascriptloops');
