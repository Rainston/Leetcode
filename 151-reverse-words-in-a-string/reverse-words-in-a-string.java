class Solution {
    public String reverseWords(String s) {
        String[] words=s.trim().split("\\s+");
        StringBuilder st= new StringBuilder();
        for(int i=words.length-1;i>=0;i--){
            st.append(words[i]+" ");
        }
        return st.toString().trim();
        

    }
}