package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2738 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int n= Integer.parseInt(st.nextToken());
        int m= Integer.parseInt(st.nextToken());

        int[][] arr= new int[n * 2][m];

        for (int i =0; i<n*2; i++){
            StringTokenizer str= new StringTokenizer(br.readLine()," ");
            for(int j =0; j<m; j++){
                arr[i][j]= Integer.parseInt(str.nextToken());
            }
        }
        for (int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                int res = arr[i][j]+arr[i+n][j];
                System.out.print(res+" ");
            }
            System.out.println();
        }
    }
}
/* 이것은 위에랑 같은 코드이다. 단, 위에서는 a, b 행렬을 나누지 않고 한 행렬에서 풀었다면, 아래는 a,b 행렬을 나누어서 풀었다.
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		// n*m 행렬
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int[][] a = new int[n][m];
		int[][] b = new int[n][m];
		StringBuilder sb = new StringBuilder();
		for(int i = 0;i<n;i++) { // a행렬
			st = new StringTokenizer(br.readLine()," ");
			for(int j = 0;j<m;j++) {
				a[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for(int i = 0;i<n;i++) { // b행렬
			st = new StringTokenizer(br.readLine()," ");
			for(int j = 0;j<m;j++) {
				b[i][j] = Integer.parseInt(st.nextToken());
				sb.append(a[i][j]+b[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

}

 */
