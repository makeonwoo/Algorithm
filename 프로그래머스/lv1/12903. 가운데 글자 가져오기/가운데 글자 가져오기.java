class Solution {
    public String solution(String s) {
        String answer = "";
        int a=s.length();
        if(a%2 == 0){
            answer += s.charAt(a/2-1);
            answer += s.charAt(a/2);
        }

        else answer += s.charAt(a/2);
        return answer;
    }
}