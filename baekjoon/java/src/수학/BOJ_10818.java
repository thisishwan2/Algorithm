package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st =new StringTokenizer(br.readLine(), " ");

        int[] nums = new int[n];
        int idx=0;
        while(st.hasMoreElements()){ //hasMoreTokens() 는 StringTokenizer 에 토큰이 남아있으면 true, 비어있으면 false를 반환한다.)
            nums[idx]=Integer.parseInt(st.nextToken());
            idx++;
        }
        //자바에서 배열의 최대 최소 구하는 쉬운 방법은 sort, for문이다.
        Arrays.sort(nums);
        System.out.print(nums[0]+" "+nums[n-1]);

    }
    //배열을 사용하지 않는 가장 빠른 방법
    //입력받은 문자를 즉시 비교
    public void fast_time_sol() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer.parseInt(br.readLine());	//첫 줄 N 은 안쓰이므로 입력만 받는다.
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        //문제의 범위
        int max = -1000001;
        int min = 1000001;

        while(st.hasMoreTokens()) {
            int val = Integer.parseInt(st.nextToken());
            if(val>max) {
                max = val;
            }
            if(val<min) {
                min = val;
            }
        }
        System.out.println(min + " " + max);
    }
}

