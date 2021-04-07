const smallestCommons = (arr) => {
    const sortedArr = arr.sort((a, b) => a > b);
    let smallestCommon = 0;
    let multiple = sortedArr[1];

    while(smallestCommon === 0){
        for(let i = sortedArr[0]; i <= sortedArr[1]; i++){
            if(multiple % i !== 0){
                break;
            }

            if(i === sortedArr[1]){
                smallestCommon = multiple;
            }
        }

        multiple += sortedArr[1];
    }
    console.log(smallestCommon);
    return smallestCommon;
}

smallestCommons([1, 5]);
smallestCommons([5, 1]);
smallestCommons([2, 10]);
smallestCommons([1, 13]);
smallestCommons([23, 18]);
