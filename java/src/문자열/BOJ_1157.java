package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1157 {
    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        String word=br.readLine().toUpperCase();
        int[] arr=new int[26]; //알파벳 갯수

        for(int i=0; i<word.length();i++){
            int num =word.charAt(i)-'A';
            arr[num]++;
        }

        int max=0;
        char ch='?';

        for(int i=0; i< arr.length; i++){
            if(arr[i]>max){
                max=arr[i];
                ch=(char) (i+65); //65를 더하거나, 'A'를 더하면 대문자가 나온다.
            } else if (arr[i]==max) {
                ch='?';
            }
        }
        System.out.println(ch);
    }
}

