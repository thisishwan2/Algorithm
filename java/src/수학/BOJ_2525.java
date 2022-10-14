package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine()," ");
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int take_m = Integer.parseInt(br.readLine());
        br.close();

        if (m+take_m>=60){
            h+=(m+take_m)/60;
            m=(m+take_m)%60;
            if (h>=24){
                h-=24;
            }
        }else{
            m=m+take_m;
        }
        System.out.println(h+" "+m);
    }
}
/* 더 쉬운 풀이(처음에 생각했던 풀이)
        int min = 60 * h + m;   // 시 -> 분
        min += take_m;

        int hour = (min / 60) % 24;
        int minute = min % 60;
*/