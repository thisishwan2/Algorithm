package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int r = Integer.parseInt(st.nextToken());
            String s = st.nextToken();
            char[] arr = new char[s.length()];

            for (int j = 0; j < s.length(); j++) {
                arr[j] = s.charAt(j);
            }

            for (char a : arr) {
                for (int j = 0; j < r; j++) {
                    sb.append(a);
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    //위 풀이와 크게 로직이 다르진 않지만 더 좋은 풀이
    public void sec_sol() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int r = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            for (int j = 0; j < s.length(); j++) {
                for (int k = 0; k < r; k++) {
                    sb.append(s.charAt(j));//위와 다르게 배열 생성없이 문자열에서 문자를 뽑아씀.
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
