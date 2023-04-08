package 정렬;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;


public class BOJ_2751 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        // list 계열 중 하나를 쓰면 된다.
        ArrayList<Integer> list = new ArrayList<>();

        for(int i = 0; i < N; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(list);

        for(int value : list) {
            sb.append(value).append('\n');
        }
        System.out.println(sb);
    }

    public static void countingSort() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        //수의 범위 -1000000~1000000 수가 -1000000일수도 있으므로 0이되는 인덱스를 1000000으로 생각
        boolean[] arr=new boolean[2000001];

        //2000001짜리 배열에서 입력받은 수를 다 true로 변환(중복없음)
        for(int i=0; i<n; i++){
            arr[Integer.parseInt(br.readLine())+1000000]=true;
        }

        //arr이 돌면서 true인것 출력하기(위에서 순서 상관없이 입력받은 값은 true이므로 정렬이 따로 필요 없다.
        for(int i=0; i<arr.length; i++){
            if(arr[i]){
                sb.append(i-1000000).append('\n');
            }
        }
        System.out.println(sb);

    }
}