const bubbleSort = arr => {
    let numSwaps = 0;
    for (let i = 0; i < arr.length; i++) {
        for(let j = 0; j < arr.length; j++){
            const first = arr[j];
            const second = arr[j + 1];
            if (first > second) {
                console.log('inequality');
                numSwaps++;
                arr[j] = second;
                arr[j + 1] = first;
            }
        }
    }
    console.log(`Array is sorted in ${numSwaps} swaps.`);
    console.log(`First Element: ${arr[0]}`);
    console.log(`Second Element: ${arr[arr.length - 1]}`);
}

bubbleSort([3, 2, 1]);