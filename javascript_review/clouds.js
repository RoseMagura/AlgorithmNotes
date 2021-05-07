const jumpingOnClouds = c => {
    for (let i = 0; i < cloudLength - 1; i++) {
        if ((i + 2) < cloudLength && c[(i + 2)] == 0) {    //Double
            numOfJumps++;
            i++;
        } else {          //Single
            numOfJumps++;
        }
    }
    return numOfJumps;
}

// const result = jumpingOnClouds([0, 0, 0, 1, 0, 0]); // should return 3
// const result = jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]); // should return 3
const result = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]); // should return 4
console.log(result);