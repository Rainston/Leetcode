class Solution {
    public int totalFruit(int[] fruits) {
        int maxlen =0;
        HashMap<Integer ,Integer> map = new HashMap<>();
        int r=0;
        int l=0;
        while(r!= fruits.length){
        map.put(fruits[r], map.getOrDefault(fruits[r], 0) + 1);
            if(map.size() <= 2){
                // maxlen = Math.max(maxlen , r-l+1);
                if(r-l+1 > maxlen) maxlen = r-l+1;
            }else{
                 if(map.get(fruits[l])==1){
                    map.remove(fruits[l]);
                 }else{
                    map.put(fruits[l] , map.get(fruits[l])-1);
                 }
                 l++;
            }
            r++;
        }
        return maxlen;
    }
}