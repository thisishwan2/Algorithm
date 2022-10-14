package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2884 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine()," ");
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        br.close();

        if (m<45){
            m=60-45+m;
            if(h==0){
                h=23;
            }
            else{
            h-=1;
            }
        }else{
            m-=45;
        }
        System.out.printf("%d %d",h,m);
    }
}
