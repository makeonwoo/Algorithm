class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        int count=0, count2=0;
        for(int i=0; i<lottos.length;i++){
            for(int j=0; j<win_nums.length; j++){
                if(lottos[i] == win_nums[j]){
                    count++;
                    break;
                }
            }
            if(lottos[i] == 0) count2 ++;
        }
        int sum_count,sel_count;
        sum_count= count+count2;
        sel_count= sum_count-count2;
        if(sum_count == 6) answer[0] =1;
        else if(sum_count == 5) answer[0] =2;
        else if(sum_count == 4) answer[0] =3;
        else if(sum_count == 3) answer[0] =4;
        else if(sum_count == 2) answer[0] =5;
        else answer[0] =6;
        
        if(sel_count == 6) answer[1] =1;
        else if(sel_count == 5) answer[1] =2;
        else if(sel_count == 4) answer[1] =3;
        else if(sel_count == 3) answer[1] =4;
        else if(sel_count == 2) answer[1] =5;
        else answer[1] =6;
        return answer;
    }
}