class Solution {
    public int totalFruit(int[] fruits) {
        int l=0,r=0,maxlen=0;
        int n=fruits.length;
        HashMap<Integer,Integer> hm=new HashMap<>();
        while(r<n){
            hm.put(fruits[r],hm.getOrDefault(fruits[r],0)+1);
            if(hm.size()>2){
                hm.put(fruits[l],hm.get(fruits[l])-1);
                if(hm.get(fruits[l])==0){
                    hm.remove(fruits[l]);
                }
                l++;
            }
            if(hm.size()<=2){
                maxlen=Math.max(maxlen,r-l+1);
            }
            r++;
        }
        return maxlen;
    }
}