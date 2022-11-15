package 정렬;

import java.io.*;


//카운팅 정렬을 기본적인 방법으로 했다.(시간초과)
public class BOJ_10989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());
        //여기 부분의 최대 수를 10001로 안하고 입력값의 최대값으로 변경하면 메모리 절약
        int[] count = new int[10001];
        int[] arr = new int[n];
        int[] res = new int[n];
        for(int i=0; i<n; i++){
            arr[i]= Integer.parseInt(br.readLine());
        }

        for(int i =0; i<arr.length; i++){
            count[arr[i]]++;
        }

        for (int i =1; i< count.length; i++){
            count[i]+=count[i-1];
        }

        for(int i=arr.length-1; i>=0; i--){
            int value=arr[i];
            count[value]--;
            res[count[value]]=value;
        }


        for(int a: res){
            System.out.println(a);
        }
    }
    //정답. 수가 작을때 시간과 메모리를 절약할 수 있는 방법.(숙지)
    public static void sol(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        //수의 범위(0~10000) 0제외
        int[] cnt= new int[10001];

        for(int i=0; i<n; i++){
            //입렫받은 값의 인덱스를 1증가.(카운팅 정렬)
            cnt[Integer.parseInt(br.readLine())]++;
        }

        StringBuilder sb = new StringBuilder();

        // 0은 입력범위에서 없으므로 1부터 시작
        for(int i = 1; i < 10001; i++){
            // i 값이 개수가 0 이 될 때 까지 출력 (빈도수를 의미)
            while(cnt[i] > 0){
                sb.append(i).append('\n');
                cnt[i]--;
            }
        }
        System.out.println(sb);
    }

    //최소 시간 풀이
    public static void sol2(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        //수의 범위(0~10000) 0제외
        int[] cnt = new int[10001];

        for (int i = 0; i < n; i++) {
            //입렫받은 값의 인덱스를 1증가.(카운팅 정렬)
            cnt[Integer.parseInt(br.readLine())]++;
        }

        for (int i = 1; i < cnt.length; i++) {
            //bw.write();를 하면 sout과 같이 한줄씩 출력한다. 그런데 뒤에 reapet 메서드를 통해 반복출력 횟수를 정할 수 있다.
            //즉, cnt에 0인 값들은 출력이 안되고, 중복된 값들은 중복된 횟수만큼 출력된다.
            bw.write(String.valueOf(i + "\n").repeat(cnt[i]));
        }
        //백준에서 이거 빼먹으면 틀린거로 나온다. 숙지.
        bw.close();
        br.close();
    }
}