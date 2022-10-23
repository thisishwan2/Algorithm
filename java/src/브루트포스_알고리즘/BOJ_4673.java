package 브루트포스_알고리즘;

import java.util.ArrayList;

public class BOJ_4673 {
    public static void main(String[] args) {
        //1~10000까지의 배열을 만들어놓음.(10001까지 한 이유는 아래의 for문을 1부터 돌릴것이기 때문
        boolean[] notSelfNum = new boolean[10001];

        //1부터 10000까지의 셀프넘버를 찾는다.
        for(int i=1; i<=10000; i++){
            int n =selfNum(i);  // n에 d(n)값 저장. (d(n)은 생성자가 있는 숫자임)

            if (n<=10000){
                notSelfNum[n]=true;//생성자가 있으면 true
            }
        }
        for(int j=1; j<=10000; j++){
            if(!notSelfNum[j]){//생성자가 없으면.
                System.out.println(j);//셀프넘버 출력
            }
        }
    }
    //n을 입력받을(생성자를 입력받을) 때 문제에서의 d(n)값을 반환하는 함수
    public static int selfNum(int num){//num가 n 즉, 생성자다
        //sum에 미리 입력받은 값을 저장
        int sum=num;
        // 입력받은 숫자+각자리수 를 구하는 while문
        while(num!=0){
            sum+=(num%10);// 처음 while문 돌때: sum=입력 받은 값+맨 뒷자리,
            num=num/10;// 처음 while문 돌때 입력값의 맨 뒷자리 제외하고 나머지들만 i에 저장
        }
        return sum; //d(n) 값 return
    }
}
