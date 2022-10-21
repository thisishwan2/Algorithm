package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class BOJ_8958 {
    //나의 풀이(정답)
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i =0 ; i<n; i++){
            String ox =br.readLine();
            char[] arr = ox.toCharArray();
            int cnt=0;
            int sum=0;
            for(int j=0; j<arr.length; j++){
                if ("O".equals(String.valueOf(arr[j]))){
                    cnt+=1;
                    sum+=cnt;
                }else {
                    cnt=0;
                }
            }
            System.out.println(sum);
        }
    }
    //배열을 이용해 입력값을 한번에 받고, StringBulider를 이용해 출력값을 한번에 출력
    public void sec_sol() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());


        String arr[] = new String[n];
        //입력값을 for문을 통해 한번에 받기.
        for(int i=0; i<arr.length; i++){
            arr[i]=br.readLine();
        }

        for(int i=0; i<n; i++){
            int cnt=0;
            int sum=0;

            for(int j=0; j<arr[i].length(); j++){
                if(arr[i].charAt(j)=='O'){//arr의 i번째(oxoxoo..)중 j번째 문자가 'O' 이면
                    cnt++;
                }else{
                    cnt=0;
                }
                sum+=cnt;
            }
            sb.append(sum).append("\n");//sb에 추가
        }
        System.out.println(sb);
    }
}
