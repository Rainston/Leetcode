class Solution {
    public int[] buildArray(int[] nums) {
        int k;
        int[] ans=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            k=nums[i];
            ans[i]=nums[k];
        }
        return ans;
    }
}