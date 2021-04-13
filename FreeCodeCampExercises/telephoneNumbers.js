const telephoneCheck = (str) => {
    if (str.includes('(')) {
        // check that the substring inbetween the parenteses isn't too long
        const betweenParen = str.split('(')[1].split(')')[0];

        if (betweenParen.length > 3) {
            console.log('issue with parentheses');
            return false;
        }
        if (!str.includes(')')) {
            return false;
        }
    }

    if (str.includes(')')) {
        if (!str.includes('(')) {
            return false;
        }
    }

    // check for special characters, except for parentheses and hyphen
    const regex = /^[0-9\)\(-\s]+$/g;
    if (!regex.test(str)) {
        return false;
    }

    // check for placement of hyphens
    if (str[0] === '-') {
        return false;
    }

    let sections = [];
    const parts = str.split('-');
    console.log(parts);
    parts.forEach(p => {
        if(p.includes(' ')){
            const elements = p.split(' ');
            elements.forEach(e => sections.push(e));
        } else {
            sections.push(p);
        }
    });

    if(sections.length === 3){
        if(sections[0].length !== 3 || sections[1].length !== 3 || sections[2].length !== 4) {
            return false;
        }
    } else if (sections.length === 4) {
        if(sections[0].length !== 1 || sections[1].length !== 3 || sections[2].length !== 3 || 
            sections[3].length !== 4) {
            return false;
        }
    } else {
        return false;
    }

    const digitsOnly = str.replace(/\s/g, '').replace(/-/g, '')
        .replace(/\(/g, '').replace(/\)/g, '');

    // check that country code is 1 if present
    if (digitsOnly.length === 11) {
        if (digitsOnly[0] !== '1') {
            console.log('country code is wrong', digitsOnly[0]);
            return false;
        }
    }

    // check that length is right
    if (digitsOnly.length < 10 || digitsOnly.length > 11) {
        console.log('length is incorrect');
        return false;
    }

    return true;
}

const test = (input, output) => {
    input === output ? console.log('Pass') : console.log('Fail');
}
const res = telephoneCheck('1 555-555-5555');

// console.log(res);
// console.log(telephoneCheck('(6054756961)'));
// console.log(telephoneCheck("10 (757) 622-7382"));
// console.log(telephoneCheck("-1 (757) 622-7382"));
