//
// @param {number[]} nums
// @return {number}
// 
var majorityElement = function(nums) {
    let elements = {};
    
    for (let i = 0; i < nums.length; i++) {
        elements[nums[i]] = elements[nums[i]] + 1 || 1;   
    }
    
    for (let i = 0; i < nums.length; i++) {
        if (elements[nums[i]] > nums.length / 2)  
            return nums[i];
    }
};