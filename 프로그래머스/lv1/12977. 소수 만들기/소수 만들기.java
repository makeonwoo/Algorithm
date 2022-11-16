import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int answer = -1;
        int test_num=0;
        ArrayList<Integer> sum = new ArrayList<Integer>();
        int prime_test =0;
        int a;
        for(int i =0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                for(int k=j+1;k<nums.length;k++){
                    a=nums[i]+nums[j]+nums[k];
                    for(int m=1; m<=a;m++){
                        if(a%m == 0) prime_test++;  
                    }
                    if(prime_test == 2) {
                        test_num = a;
                        sum.add(test_num);
                    }
                    prime_test=0;
                }
            }
        }
        // Set<Integer> set = new HashSet<Integer>(sum);    
        // ArrayList<Integer> newList =new ArrayList<Integer>(set);

        answer = sum.size();
        System.out.println(sum);

        return answer;
    }
}