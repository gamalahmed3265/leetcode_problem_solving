class Solution {
  int searchInsert(List<int> nums, int target) {
    for (int i=0;i<nums.length;i++){
        if (nums[i]>=target)return i;
    }
    return nums.length;
  }
}