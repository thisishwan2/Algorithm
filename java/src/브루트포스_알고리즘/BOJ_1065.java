package 브루트포스_알고리즘;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1065 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(hanSu(n));

    }

    public static int hanSu(int n) {
        int cnt = 0;
        if (n <= 99) {
            cnt = n;
        } else if (n<=1000) {
            cnt = 99;

            for (int i = 100; i <= n; i++) {
                double fir = i/100;
                double sec = (i%100)/10;
                double thi= (i%100)%10;

                if((fir+thi)/2==sec){
                    cnt+=1;
                }

            }

        }
        return cnt;
    }
}
