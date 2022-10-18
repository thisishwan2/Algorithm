package 수학;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_15552 {
    //1번 BufferedWriter을 이용
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //System.out.println();과 유사(속도 측면에서 우월)
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n =Integer.parseInt(br.readLine());

        StringTokenizer st;

        for (int i=0; i<n; i++){
            st=new StringTokenizer(br.readLine()," ");
            //버퍼에 있는 값 전부 출력
            bw.write((Integer.parseInt(st.nextToken())+Integer.parseInt(st.nextToken()))+"\n");

        }
        br.close();
        bw.flush();////남아있는 데이터를 모두 출력시킴(버퍼를 비움)
        bw.close();
    }
    //2번 StringBuilder을 이용
    public void sec_Sol() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st;
        StringBuilder sb = new StringBuilder(); //StringBuilder 객체 생성

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine()," ");
            sb.append(Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken())).append('\n');
        }
        br.close();

        System.out.println(sb);

    }
    //3번 String.substring()이용
    public void third_Sol() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            int target = str.indexOf(" ");
            int result = Integer.parseInt(str.substring(0,target)) + Integer.parseInt(str.substring(target + 1));
            sb.append(result+"\n");
        }

        br.close();
        System.out.print(sb);
    }
}
