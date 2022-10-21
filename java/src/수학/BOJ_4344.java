package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_4344 {
    //맞춘 나의 정답(너무 조잡합)
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int c = Integer.parseInt(br.readLine());

        for (int i = 0; i < c; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int fir = Integer.parseInt(st.nextToken());
            ArrayList<Integer> list=new ArrayList<>();
            for (int j = 0; j < fir; j++) {
                list.add(Integer.valueOf(st.nextToken()));
            }
            double sum=0;
            for(int num: list){
                sum+=num;
            }
            double total_avg = sum/list.size();

            double cnt=0;

            for(int num: list){
                if (num>total_avg){
                    cnt+=1;
                }
            }

            double per = cnt/list.size()*100;
            //문자열 포매팅을 이용해 3째 자리가지 표현
            System.out.println(String.format("%.3f%%",per));
        }
    }

    //아래처럼 풀수 있어야한다.
    //아래는 학생수를 먼저 뽑고, 그후 성적 배열을 따로 생성하여서 풀는 방식
    public void sec_sol() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr;

        int c = Integer.parseInt(br.readLine());
        StringTokenizer st;

        //학생수만 먼저 추출해서 성적 부분만 for문을 돌린다.
        for(int i = 0 ; i < c ; i++) {
            st = new StringTokenizer(br.readLine(), " "); // 학샐수 및 성적입력

            int n =Integer.parseInt(st.nextToken()); //학생수
            //학생수만큼 배열 길이 생성
            arr=new int[n];

            double sum=0;
            //성적부분
            for(int j=0; j<n; j++){
                int score = Integer.parseInt(st.nextToken());
                arr[j] = score;
                sum+=score;
            }

            double totalAvg = sum/n;
            double cnt=0;

            for(int j=0; j<n; j++){
                if(arr[j]>totalAvg){
                    cnt++;
                }
            }
            System.out.printf("%.3f%%\n",(cnt/n)*100);

        }
    }

}
