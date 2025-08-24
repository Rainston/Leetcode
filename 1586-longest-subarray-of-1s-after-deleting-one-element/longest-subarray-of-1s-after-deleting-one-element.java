class Solution {
    public int longestSubarray(int[] nums) {
        int l=0,r=0,zeros=0,len=0;
        int n=nums.length;
        while(r<n){
            if(nums[r]==0){
                zeros+=1;
            }
            while(l<=n && zeros>1){
                if(nums[l]==0){
                    zeros--;
                }
                l++;
            }
            len=Math.max(len,r-l);
            r++;
        }
        return len;
    }
}