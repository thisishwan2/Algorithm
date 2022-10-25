package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
//boolean을 이용하여 검은 부분의 좌표(점)마다 true값을 넣어주고, 넓이를 구하는 문제.
public class BOJ_2563 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int paperNum = Integer.parseInt(br.readLine()); //색종이 개수

        boolean[][] arr = new boolean[101][101];    //도화지(처음 논리값 배열을 만들면 false값이 들어있음.
        int total = 0;  //검은영역 넓이(true 범위)


        for (int i = 0; i < paperNum; i++) {
            StringTokenizer a = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(a.nextToken());
            int y = Integer.parseInt(a.nextToken());

            for (int j = x; j < x + 10; j++) {
                for (int k = y; k < y + 10; k++) {
                    if (!arr[j][k]) {//만약 해당부분(점이라고 생각하는게 편함)이 false이면,
                        arr[j][k] = true;   //true값을 저장해주고
                        total++;            //검은영역에 1을 더함
                    }//이렇게 하면 중복된 검은 부분은 한번만 true입력됨.
                }

            }
        }
        System.out.println(total);
    }
}