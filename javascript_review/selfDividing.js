/** Input:
* left = 1, right = 22
* Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
*/

const selfDividing = (left, right) => {
    const output = new Set();
    let curr = left;
    while (curr <= right) {
        if (curr < 10) {
            output.add(curr); // for numbers less than 10
        } else {
            let passing = true;
            for (let i in String(curr)) {
                const digit = parseInt(String(curr)[i]);
                if (digit === 0 || curr % digit !== 0) {
                    passing = false;
                    break;
                }
            }
            if (passing) {
                output.add(curr);
            }
        }
        curr++;
    }
    console.log(output);
    return output;
}

const alternateSolution = (left, right) => {
    const result = [];
    const selfDividingTest = num => {
        return num.toString().split('').every(letter => {
            if (Number(letter) === 0 || num % Number(letter) !== 0) {
                return false;
            }
            return true;
        })
    }

    for (let i = left; i <= right; i++) {
        if (selfDividingTest(i)) {
            result.push(i);
        }
    }
    return result;
}

selfDividing(1, 22);
selfDividing(10, 13);