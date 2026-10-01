class Solution {
    public boolean isPalindrome(int x) {
        int rem =0;
        int flag=0;
        int original =x;
        int ans=0;
        while(x>0){
                rem=x%10;
                ans=ans*10 + rem;
                x=x/10;
        }
        if (ans==original){
            flag=1;
        }
        if(flag==1){
            return true;
        }
        else{
            return false;
        }


    }
}