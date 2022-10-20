package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class BOJ_1110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int staticNum=num;
        int cnt = 1;
        while (true) {
            int fir = num / 10;
            int sec = num % 10;
            int sum = (fir + sec)%10;
            int new_num = Integer.parseInt(String.valueOf(sec) + String.valueOf(sum));

            if (new_num == staticNum) {
                System.out.println(cnt);
                break;
            } else {
                num=new_num;
                cnt++;
            }

        }

    }
    public void sec() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int cnt = 0;
        int copy = N;

        do {
            N = ((N % 10) * 10) + (((N / 10) + (N % 10)) % 10);
            cnt++;
        } while (copy != N);

        System.out.println(cnt);
    }
}