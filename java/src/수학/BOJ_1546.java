package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1546 {
    //핵심! 자바는 파이썬과는 다르게 //가 / %가%이다. 즉, 파이썬에서의 / 연산이 없다.
    //따라서 변수자체를 정수가 아닌 소수로 선언해줘야 파이썬의 /와 같은 연산이 가능하다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double arr[] = new double[Integer.parseInt(br.readLine())];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for(int i=0; i< arr.length; i++){
            arr[i]=Double.parseDouble(st.nextToken());
        }

        double sum=0;
        Arrays.sort(arr);

        for(int i =0; i< arr.length; i++){
            sum+=(arr[i]/arr[ arr.length-1])*100;
        }
        System.out.println(sum/ arr.length);
    }
}
