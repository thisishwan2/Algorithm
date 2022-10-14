package 수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2588 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num1 = Integer.parseInt(br.readLine());
        int num2 = Integer.parseInt(br.readLine());
        br.close();
        int n100 =num2/100;
        int n10 =(num2%100)/10;
        int n1 =num2%10;

        System.out.println(num1*n1);
        System.out.println(num1*n10);
        System.out.println(num1*n100);
        System.out.println(num1*num2);

    }

}
/*
        int num1 = Integer.parseInt(br.readLine());
        String num2 = br.readLine();
        br.close();
        System.out.println(num1 * (num2.charAt(2) - '0'));
        System.out.println(num1 * (num2.charAt(1) - '0'));
        System.out.println(num1 * (num2.charAt(0) - '0'));
        System.out.println(num1 * Integer.parseInt(num2));
        num2는 charAt()으로 각 자리수를 참조한다.
        이때 반환되는 값은 아스키 코드값인 문자(char)이다.
        각각의 문자열 인덱스를 참조한 뒤 -'0' 을 해주는 이유는 우리가 문자로 저장된 숫자가 아닌/ 우리가 보는 숫자 그대로의 값을 쓰기 위한 것이다.

        또 다른 방법은
        int num1 = Integer.parseInt(br.readLine());
        String num2 = br.readLine();
        br.close();

        char[] num = num2.toCharArray(); //문자열을 char 배열 형태로 반환해주는 메소드가 있다.

        System.out.println(num1 * (b[2] - '0'));
        System.out.println(num1 * (b[1] - '0'));
        System.out.println(num1 * (b[0] - '0'));
        System.out.println(num1 * Integer.parseInt(num2));
 */
