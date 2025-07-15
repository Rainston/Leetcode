class Solution {
    public boolean isValid(String word) {
        int n=word.length();
        if(n<3){
            return false;
        }
        int v=0,cs=0;
        for(char c : word.toCharArray()){
            if(Character.isLetter(c)){
                if("aeiouAEIOU".indexOf(c)!=-1){
                    v++;
                }
                else{
                    cs++;
                }
            }
            else if(!Character.isDigit(c)){
                return false;
            }
        }
        return v>=1 && cs>=1;
    }
}