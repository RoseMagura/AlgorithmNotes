const rot13 = (str) => {
    let decodedChars = [];
    for (let index in str) {
        const encoded = str.charCodeAt(index);
        if (encoded > 90 || encoded < 65) {
            decodedChars.push(str[index]);
            continue;
        }

        if (encoded > 77) {
            const decoded = String.fromCharCode(encoded - 13);
            decodedChars.push(decoded);
        } else {
            const decoded = String.fromCharCode(encoded + 13);
            decodedChars.push(decoded);
        }
    }
    return decodedChars.join('');
}

console.log(rot13('SERR PBQR PNZC'));
console.log(rot13('SERR CVMMN!'));
console.log(rot13('SERR YBIR?'));
console.log(rot13('GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.'));