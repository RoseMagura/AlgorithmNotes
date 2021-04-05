function uniteUnique (arr) {
    let uniqueArr = [];
    for(let subarray in arguments) {
        for(let index in arguments[subarray]){
            const val = arguments[subarray][index];
            if(!uniqueArr.includes(val)){
                uniqueArr.push(val);
            }
        }
    }
    return uniqueArr;
};
  
uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);