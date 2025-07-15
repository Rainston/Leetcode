class Solution {
    public int longestOnes(int[] nums, int k) {
        int l=0,r=0,zro=0,maxlen=0;
        int n=nums.length;
        while(r<n){
            if(nums[r]==0){
                zro++;
            }
            if(zro>k){
                if(nums[l]==0){
                    zro--;
                }
                l++;
            }
            if(zro<=k){
                int len=r-l+1;
                maxlen=Math.max(len,maxlen);
            }
            r++;
        }
        return maxlen;
    }
}