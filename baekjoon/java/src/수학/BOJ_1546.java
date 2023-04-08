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
        //arr를 double형으로 선언
        double arr[] = new double[Integer.parseInt(br.readLine())];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for(int i=0; i< arr.length; i++){
            arr[i]=Double.parseDouble(st.nextToken());//입력받은 문자를 double형으로
        }

        double sum=0;
        Arrays.sort(arr);

        for(int i =0; i< arr.length; i++){
            sum+=(arr[i]/arr[ arr.length-1])*100;
        }
        System.out.println(sum/ arr.length);
    }
    //자동형변환을 이용하여 sum만 double형 타입이고,나머지는 int형 타입이다.

    public void sec_col() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); //입력 개수

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        //입력값이 0보다 크거나 같음.
        int max = -1;
        double sum = 0.0;

        for (int i = 0; i < N; i++) {
            int value = Integer.parseInt(st.nextToken());

            if(value > max) {
                max = value;
            }

            sum += value;
        }

        System.out.println(((sum / max) * 100.0) / N);
        // 참고로 오차범위가 데이터가 sum이 double형인 것이 명확하고 실수할 것이 없기에 자동형변환을 사용해도 된다.
        //만약 데이터가 너무 다양해지거나, 제한 된 데이터형들이 존재하게 될 경우 실수 할 수도 있기 때문에 안전하게 모두 double형으로 선언해주는 것이 안전하긴 하다.
    }
}
