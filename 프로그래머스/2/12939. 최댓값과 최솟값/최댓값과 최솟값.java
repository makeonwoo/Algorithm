import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
        String[] shorts = s.split(" ");
        int max = Integer.parseInt(shorts[0]);
        int min = Integer.parseInt(shorts[0]);
        
        for (String tmp : shorts){
            int tmpNumber = Integer.parseInt(tmp);
            if (max < tmpNumber){
                max = tmpNumber;
            }
            if (min > tmpNumber){
                min = tmpNumber;
            }
        }
        return min +" " + max ;
    }
}