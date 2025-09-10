class Solution {
    public boolean isHappy(int n) {
        int fast=n;
        int slow=n;
        do{
            slow=findSquare(slow);
            fast=findSquare(findSquare(fast));
            if(slow==1){
                return true;
            }
        }while(slow!=fast);

        return false;
    }
    private int findSquare(int n){
        int val=0;
        while(n>0){
            int r=n%10;
            val+=r*r;
            n/=10;
        }
        return val;
    }
}