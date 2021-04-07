const translatePigLatin = (str) => {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    // if word begins with vowel
    if (vowels.includes(str[0])) {
        return str + 'way';
    }

    // if word begins with consonant(s)
    let consonants = [];
    for(let index in str){
        if(vowels.includes(str[index])){
            return str.slice(index) + consonants.join('') + 'ay';
        } else {
            consonants.push(str[index]);
        }
    }
    //  if no vowels
    return str + 'ay';
}

const test = (input, output) => {
    input === output ? console.log('Pass') : console.log('Fail');
}

test(translatePigLatin('algorithm'), 'algorithmway');
test(translatePigLatin('rhythm'), 'rhythmay');
test(translatePigLatin('eight'), 'eightway');

test(translatePigLatin('california'), 'aliforniacay');
test(translatePigLatin('paragraphs'), 'aragraphspay');
test(translatePigLatin('glove'), 'oveglay');
test(translatePigLatin('schwartz'), 'artzschway');
test(translatePigLatin('consonant'), 'onsonantcay');
