function reverseString(str) {
  const arr = str.split('');
  return arr.reverse().join('');
}

console.log(reverseString('hello') === 'olleh' ? 'Pass' :'Fail');
console.log(reverseString('Howdy') === 'ydwoH' ? 'Pass' :'Fail');
console.log(reverseString('Greetings from Earth') === 'htraE morf sgniteerG' ? 'Pass' :'Fail');
