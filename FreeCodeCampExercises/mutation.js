const mutation = (arr) => {
    const lowerArr = arr[0].toLowerCase();
    for (let index = 0; index < arr[1].length; index++) {
        const char = arr[1][index].toLowerCase();
        if (lowerArr.indexOf(char) < 0) {
            return false;
        }
    }
    return true;
}

console.log(mutation(['hello', 'hey'])); // should return false
console.log(mutation(['hello', 'Hello'])); // should return true
console.log(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])); //should return true