var removeDuplicates = (nums) => {
    // set pointers to the initial value
    [left, right] = [0, 0];
    // move right pointer through every element
    while (right < nums.length) {
        const [leftVal, rightVal] = [nums[left], nums[right]];
        // check if current val is equal to previous val
        const isEqual = (leftVal === rightVal);
        if  (!isEqual) {
            // move left pointer to next index
            left++;
            nums[left] = rightVal;
        }
        right++;
    }
    return (left + 1);
};