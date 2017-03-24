/**
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 * 
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var i = nums.length-1;
    
    while(i > 0) {
        if (nums[i] === nums[i-1]) {
            nums.splice(i,1);
        }
        i--;
    }
    return nums.length;
};