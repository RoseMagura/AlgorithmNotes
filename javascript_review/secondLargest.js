/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
const getSecondLargest = (nums) => {
    let first = nums[0];
    let second = -1;
    for(let i in nums){
        if(nums[i] > first){
            second = first;
            first = nums[i];
        }

        if(nums[i] > second && nums[i] < first){
            second = nums[i];
        }
    }
    return second;
}

const testOne = getSecondLargest([2, 3, 6, 6, 5]);
console.log(testOne);