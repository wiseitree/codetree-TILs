import java.util.Scanner;

public class Main {
    public static final int ASCII_NUM = 128;
    public static int n, currX, currY, elapsedTime, dir, ans = -1;
    public static int[] dxs = new int[]{0, 1, 0, -1};
    public static int[] dys = new int[]{1, 0, -1, 0};
    public static int[] mapper = new int[ASCII_NUM];





    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        mapper['E'] = 0;
        mapper['S'] = 1;
        mapper['W'] = 2;
        mapper['N'] = 3;

        for (int i = 0; i < n; i++) {
            char cDir = sc.next().charAt(0);
            int t = sc.nextInt();
            dir = mapper[cDir];

            for (int j = 0; j < t; j++) {
                currX = currX + dxs[dir];
                currY = currY + dys[dir];
                elapsedTime++;

                if(currX == 0 && currY == 0) {
                    ans = elapsedTime;
                    System.out.println(ans);
                    System.exit(0);
                }
            }

        }

        System.out.println(ans);
    }
}