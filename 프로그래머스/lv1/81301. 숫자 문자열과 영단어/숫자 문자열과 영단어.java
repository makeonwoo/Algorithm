class Solution {
    public int solution(String s) {
        int answer = 0;
        //int[] num = new int[50];
        String num = "";
        String sumString ="";
        
        for(int i=0; i<s.length();i++){
            if(Character.isDigit(s.charAt(i))){
                num += s.charAt(i);
            }
            else{
                sumString += s.charAt(i);
            }
            if(sumString.equals("zero")){
                num += "0";
                sumString = "";
            } 
            else if(sumString.equals("one")) {
                num += "1";
                sumString = "";
            } 
            else if(sumString.equals("two")) {
                num += "2";
                sumString = "";
            } 
            else if(sumString.equals("three")) {
                num += "3";
                sumString = "";
            } 
            else if(sumString.equals("four")) {
                num += "4";
                sumString = "";
            } 
            else if(sumString.equals("five")) {
                num += "5";
                sumString = "";
            } 
            else if(sumString.equals("six")) {
                num += "6";
                sumString = "";
            } 
            else if(sumString.equals("seven")) {
                num += "7";
                sumString = "";
            } 
            else if(sumString.equals("eight")) {
                num += "8";
                sumString = "";
            } 
            else if(sumString.equals("nine")) {
                num += "9";
                sumString = "";
            } 
}
        answer = Integer.parseInt(num);
        return answer;
    }
}