/*
You are given an integer array nums. The unique elements of an array are 
the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Examples:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Source: LeetCode
*/

const uniqueSum = nums => {
    const unique = new Set();
    const alreadyUsed = new Set();
    nums.forEach(element => {
        if(!alreadyUsed.has(element)){
            unique.add(element);
            alreadyUsed.add(element);
        } else {
            unique.delete(element);
        }
    });

    if(unique.size === 0){
        console.log(0);
        return 0;
    }
    const sum = Array.from(unique).reduce((sum, number) => sum + number);
    console.log(sum);
    return sum;
}

const alternateSolution = nums => {
    const map = {};
    let sum = 0;

    for(const num of nums){
        map[num] = map[num] + 1 || 1;
    }

    for(const key in map){
        if(map[key] > 2){
            sum += Number(key);
        }
    }
    return sum;
}

const testOne = uniqueSum([1, 2, 3, 2]); // should return 4
const testTwo = uniqueSum([1, 1, 1, 1, 1]); // should return 0
const testThree = uniqueSum([1, 2, 3, 4, 5]); // should return 15

// time complexity is O(n)