const telephoneCheck = (str) => {
    // const countryCode = str.split(' ');
    const patt = new RegExp(/^\d/);
    return patt.test(str);
}

// const res = telephoneCheck('5');
const res = telephoneCheck('555-555-5555');
// const res = telephoneCheck('-1 300');
console.log(res);