class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0,r=0,maxlen=0;
        int n= s.length();
        HashSet<Character> hash=new HashSet<>();
        while(r<n){
            if(!hash.contains(s.charAt(r))){
                hash.add(s.charAt(r));
                r++;
                maxlen=Math.max(hash.size(),maxlen);
            }
            else{
                hash.remove(s.charAt(l));
                l++;
            }
        }
        return maxlen;
    }
}