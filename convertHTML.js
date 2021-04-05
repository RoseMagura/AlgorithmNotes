function convertHTML(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

console.log(convertHTML("Dolce & Gabbana"));
console.log(convertHTML('abc'));
console.log(convertHTML('Hamburgers < Pizza < Tacos'));
console.log(convertHTML("Schindler's List"));
console.log(convertHTML('Stuff in "quotation marks"'));