class Solution {
    public int solution(int n) {
        int answer = 0;
        String revers = "";
        int temp = 0;
        char r,ss; 
        final String s = Integer.toString(n, 3);
        for(int i= s.length()-1; i>=0; i--){
            ss=s.charAt(i);
            revers += ss;
        }
        for(int i = revers.length()-1;i>=0;i--){          
            answer+=((revers.charAt(i) - '0') * (int)Math.pow(3,temp));         
            temp++;
        }
        return answer;
    }
}