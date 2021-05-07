const jumpingOnClouds = c => {
    let allPossible = [];
    let currPos = 0;
    let jumps = 0;
    // one length jump
    while(currPos < c.length){
        if(c[currPos + 1] === 1) {
            currPos += 2;
            jumps++;
            continue;
        }
        currPos++;
        if(currPos > c.length){
            break;
        }
        jumps++;
    }
    allPossible.push(jumps);
    // reset
    jumps = 0;
    currPos = 0;
    // two length jump
    while(currPos < c.length){
        console.log(c[currPos], currPos);
        if(c[currPos + 2] === 1) {
            console.log('danger');
            currPos++;
            jumps++;
            continue;
        }
        currPos += 2;
        if(currPos > c.length){
            console.log('breaking', currPos);
            break;
        }
        jumps++;

    }
    allPossible.push(jumps);
    return allPossible[0] <= allPossible[1] 
        ? allPossible[0]
        : allPossible[1];
}

// const result = jumpingOnClouds([0, 0, 0, 1, 0, 0]); // should return 3
// const result = jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]); // should return 3
const result = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]); // should return 4
console.log(result);