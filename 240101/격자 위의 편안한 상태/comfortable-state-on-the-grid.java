import java.util.Scanner;

public class Main {
    public static final int MAX_N = 100;
    public static int n, m, x, y;
    public static int[] dxs = new int[]{-1, 1, 0, 0};
    public static int[] dys = new int[]{0, 0, -1, 1};
    public static int[][] grid = new int[MAX_N][MAX_N];
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < m; i++) {
            int r = sc.nextInt();
            int c = sc.nextInt();
            x = r-1; y = c-1;
            
            grid[x][y] = 1;

            if(isComfort(x, y))
                System.out.println(1);
            else
                System.out.println(0);
        }
        
        
    }

    private static boolean isComfort(int x, int y) {
        int cnt = 0;

        for (int i = 0; i < 4; i++) {
            int nx = x + dxs[i], ny = y + dys[i];

            if(inRange(nx, ny) && grid[nx][ny] == 1)
                cnt++;
        }
        
        return cnt == 3;
    }

    private static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }
    
}