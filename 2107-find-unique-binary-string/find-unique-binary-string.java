class Solution {
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder res=new StringBuilder();
        for(int i=0;i<nums.length;i++){
            Character cu=nums[i].charAt(i);
            res.append(cu=='0'?'1':'0');
        }
        return res.toString();
    }
}