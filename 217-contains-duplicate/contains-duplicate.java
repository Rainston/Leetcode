class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> se=new HashSet<>();
        for(int n:nums){
            if(se.contains(n)){
                return true;
            }
            se.add(n);
        }
        return false;
    }
}