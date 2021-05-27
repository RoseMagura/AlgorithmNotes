/**
 * @param {string[]} words
 * @return {string[]}
 * Source: LeetCode
 */
const keyboardRow = words => {
    const output = [];
    const map = {
        'q': 1,
        'w': 1,
        'e': 1,
        'r': 1,
        't': 1,
        'y': 1,
        'u': 1,
        'i': 1,
        'o': 1,
        'p': 1,
        'a': 2,
        's': 2,
        'd': 2,
        'f': 2,
        'g': 2,
        'h': 2,
        'j': 2,
        'k': 2,
        'l': 2,
        'z': 3,
        'x': 3,
        'c': 3,
        'v': 3,
        'b': 3,
        'n': 3,
        'm': 3
    }

    for (let i in words) {
        const orig = words[i];
        const currWord = words[i].toLowerCase();
        const row = map[currWord[0]];
        let j = 1;
        while (map[currWord[j]] === row) {
            j++;
        }
        if (j === currWord.length) {
            output.push(orig);
        }
    }
    return output;
}
// Time Complexity is O(n^2)

// From discussion board (notes about a faster method)
const alternateSolution = words => {
    const row1 = new Set("qwertyuiop");
    const row2 = new Set("asdfghjkl");
    const row3 = new Set("zxcvbnm");

    const res = [];

    for (const word of words) {
        if (canBeTyped(word, row1) || canBeTyped(word, row2) || canBeTyped(word, row3)) res.push(word);
    }

    return res;

    function canBeTyped(word, row) {
        for (const char of word) {
            if (!row.has(char.toLowerCase())) return false;
        }
        return true;
    }
};

keyboardRow(["Hello", "Alaska", "Dad", "Peace"]); // should return ['Alaska', 'Dad']
keyboardRow(['omk']); // should return []
keyboardRow(['adsdf', 'sfd']); // should return ['adsdf', 'sfd']