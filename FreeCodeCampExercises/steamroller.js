const steamrollArray = (arr) => {
    let flatArr = [];
    for(const index in arr) {
        append(arr[index], flatArr);

        let currArr = arr[index];
        while(currArr.length > 0) {
            let val = currArr.shift();
            // const isArray = append(val, flatArr);
            // console.log(val, isArray)
            if(!Array.isArray(val)){
                append(val, flatArr);
            } else {
            while(Array.isArray(val)) {
                val = val.pop();
                console.log(val);
            }
            console.log('val at end', val);
            append(val, flatArr);}
        }
    }
    console.log(flatArr);
    return flatArr;
}

const append = (value, array) => {
    if(!Array.isArray(value)){
        array.push(value);
    } 
    return Array.isArray(value);
}

// steamrollArray([1, [2], [3, [[4]]]]);
// console.log(steamrollArray([[["a"]], [["b"]]]));
// steamrollArray([1, [], [3, [[4]]]]);
steamrollArray([1, {}, [3, [[4]]]]);