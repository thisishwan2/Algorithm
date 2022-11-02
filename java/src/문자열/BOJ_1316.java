package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1316 {
    //br을 여러 메서드에서 사용하기 위해 main밖으로 빼서 static선언 해준다.
    static BufferedReader br =new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int cnt=0;
        //check 메서드가 true면 그룹단어이다.
        for (int i=0; i<n; i++){
            if (check()==true){
                cnt++;
            }
        }
        System.out.println(cnt);
    }
    //그룹단어 임을 체크하는 메서드
    public static boolean check() throws IOException {
        //알파벳이 26개이므로 사용하면 true로 바뀔 수 있도록 26크기의 boolean 배열을 만든다.
        boolean[] check=new boolean[26];
        String str= br.readLine();//단어를 입력받는다.

        int prev=0;
        //단어의 각 알파벳을 검사한다.
        for(int i=0; i<str.length(); i++) {
            int now = str.charAt(i);//i 번째 문자 저장 (현재 문자)
            // 앞선 문자와 i 번째 문자가 같지 않다면?
            if (prev !=now){
                //해당 문자가 처음 나오는 경우
                if (check[now-'a']==false){
                    check[now-'a']=true;//사용됐다는 의미로 true로 변경
                    prev=now;//다음 턴을 위해 prev에 now를 저장
                }
                //이미 나왔다면 그룹단어가 아니다.
                else{
                    return false;
                }
            }
        }
        // 문자열을 아무이상없이 다 돌았으면 true
        return true;
    }
}