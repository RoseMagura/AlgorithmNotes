const n = 5;
const binary = (n >>> 0).toString(2);
let consec = 0;
for(let i = 0; i < binary.length; i++){
    if(binary[i] === '1'){
        consec++;
    } else {
        break;
    }
}

let backwardsConsec = 0;
for(let i = binary.length - 1; i >= 0; i--){
    if(binary[i] === '1'){
        backwardsConsec++;
    } else {
        break;
    }
}

consec > backwardsConsec 
    ? console.log(consec) 
    : console.log(backwardsConsec);

// More efficient solution from HackerRack discussion
const solution = () => {
    console.log(n.toString(2).split('0').sort((a, b) => a < b)[0].length);
}

solution();