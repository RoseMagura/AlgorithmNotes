/*
Given an array words of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within 
the list (including duplicates). For example, if a character occurs 3 times 
in all strings but not 4 times, you need to include that character three times 
in the final answer.

You may return the answer in any order.

Examples:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Input: ["cool","lock","cook"]
Output: ["c","o"]

Source: Leet Code
*/

const commonChar = words => {
    const output = [];
    const alreadyUsed = new Set();
    for (let i in words[0]) {
        const re = new RegExp(words[0][i], 'g');
        let min = 0;
        if (!alreadyUsed.has(words[0][i])) {
            const count = words[0].match(re).length;
            min = count;
        }
        for (let j = 1; j < words.length; j++) {
            const localMatch = words[j].match(re);
            if(!alreadyUsed.has(words[0][i]) && localMatch !== null){
                if(localMatch.length < min){
                    min = localMatch.length;
                }
            } else if(localMatch === null){
                min = 0;
            }
        }
        // add the character as many times as it showed up in all strings
        while(min > 0){
            output.push(words[0][i]);
            min--;
        }
        alreadyUsed.add(words[0][i]);
    }
    console.log(output);
    return output;
}

// commonChar(["bella", "label", "roller"]);
commonChar(["cool","lock","cook"]); 