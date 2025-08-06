class Solution {
    public int characterReplacement(String s, int k) {
        int l=0,r=0;
        int maxf=0,maxlen=0;
        int n=s.length();
        int []p=new int[26];
        while(r<n){
            p[s.charAt(r)-'A']++;
            maxf=Math.max(maxf,p[s.charAt(r)-'A']);
            if((r-l+1)-maxf>k){
                p[s.charAt(l)-'A']--;
                l++;
            }
            maxlen=Math.max(maxlen,r-l+1);
            r++;
        }
        return maxlen;
    }
}