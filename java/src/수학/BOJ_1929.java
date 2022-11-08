package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1929 {

    public static boolean prime[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine(), " ");

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        prime = new boolean[n+1];
        primeNum();

        for(int i=m; i<=n; i++){
            if(prime[i]==false){
                System.out.println(i);
            }
        }



    }

    public static void primeNum(){
        prime[0]=true;
        prime[1]=true;

        for (int i=2; i<=Math.sqrt(prime.length); i++){
            if(prime[i]){
                continue;
            }for(int j=i*i; j<prime.length; j+=i){
                prime[j]=true;
            }
        }
    }
}