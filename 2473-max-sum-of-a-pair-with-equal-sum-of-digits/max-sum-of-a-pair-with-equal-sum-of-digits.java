class Solution {
    private int getdigitsum(int val){
        int sum=0;
        while(val!=0){
            sum+=val%10;
            val/=10;
        }
        return sum;
    } 
    public int maximumSum(int[] nums) {
        Map<Integer, Integer> sumMaxVal = new HashMap<>();
        int maxsum=-1;
        for(int i:nums){
            int digitsum=getdigitsum(i);
           if (sumMaxVal.containsKey(digitsum))
           {
            maxsum=Math.max(maxsum,i+sumMaxVal.get(digitsum));
            if(sumMaxVal.get(digitsum) < i){
              sumMaxVal.put(digitsum,i);
            }
           }
           else{
            sumMaxVal.put(digitsum,i);
           }
        }
        return maxsum;
        
        
    }
}