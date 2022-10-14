import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int king=1;
        int queen=1;
        int rook=2;
        int bishop=2;
        int knight=2;
        int pawn=8;
        king =king- Integer.parseInt(st.nextToken());
        queen =queen- Integer.parseInt(st.nextToken());
        rook =rook-  Integer.parseInt(st.nextToken());
        bishop =bishop- Integer.parseInt(st.nextToken());
        knight =knight- Integer.parseInt(st.nextToken());
        pawn =pawn- Integer.parseInt(st.nextToken());

        System.out.printf(king+" "+queen+" "+rook+" "+bishop+" "+knight+" "+pawn);


    }
}
