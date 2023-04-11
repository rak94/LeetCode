var removeDuplicates = (nums) => {
    [left, right] = [0, 0];
    while (right < nums.length) {
        const [leftVal, rightVal] = [nums[left], nums[right]];
        const isEqual = (leftVal === rightVal);
        if  (!isEqual) {
            left++;
            nums[left] = rightVal;
        }
        right++;
    }
    return (left + 1);
};