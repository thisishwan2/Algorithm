package 수학;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class BOJ_9020 {
    public static boolean[] prime = new boolean[10001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        getPrime();
        int t = Integer.parseInt(br.readLine());
        //while(t-- >0) 이건 t--; t>0이 합쳐진 것임. 기억해두기.
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int p = n/2;
            int q = n/2;
            while(true) {
                if (!prime[p] && !prime[q]) {
                    sb.append(p + " " + q).append('\n');
                    break;
                }

                p--;
                q++;
            }
        }
        System.out.println(sb);
    }

    public static void getPrime(){
        prime[0]=prime[1]=true;

        for(int i=2; i<=Math.sqrt(prime.length); i++){
            if(prime[i]) continue;
            for(int j=i*i; j< prime.length; j+=i){
                prime[j]=true;
            }
        }
    }
}