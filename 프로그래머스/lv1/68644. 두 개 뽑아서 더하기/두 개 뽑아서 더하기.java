import java.util.ArrayList;
import java.util.HashSet;
import java.util.Comparator;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        ArrayList<Integer> sum = new ArrayList<Integer>();
        for(int i=0; i<numbers.length;i++){
            for(int j=0; j<numbers.length;j++){
                if(i != j)
                    sum.add(numbers[i]+numbers[j]);
            }
        }
        HashSet<Integer> a = new HashSet<Integer>(sum);
        ArrayList<Integer> sum2 = new ArrayList<Integer>(a);
        sum2.sort(Comparator.naturalOrder());
        System.out.println(sum2);
        answer = new int[sum2.size()];
        for(int m=0; m< sum2.size();m++){
            answer[m] = sum2.get(m);
        }
        return answer;
    }
}