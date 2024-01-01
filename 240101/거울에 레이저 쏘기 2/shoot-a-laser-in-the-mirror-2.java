import java.util.Scanner;

public class Main {
    public static int x, y, dir;
    public static int[] dxs = new int[]{1, 0, -1, 0};
    public static int[] dys = new int[]{0, -1, 0, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] grid = new String[n];

        for (int i = 0; i < n; i++)
            grid[i] = sc.next();
        int k = sc.nextInt();

        init(n, k);
        
        int cnt = 0;
        while (true){
            int nx = x + dxs[dir], ny = y + dys[dir];
            if (!inRange(nx, ny, n))
                break;
            cnt++;
            dir = getNextDir(nx, ny, dir, grid);
            x = nx; y = ny;
        }

        System.out.println(cnt);

    }

    private static int getNextDir(int x, int y, int dir, String[] grid) {
        if (grid[x].charAt(y) == '\\')
            return 3 - dir;
        else
            return dir ^ 1;
    }

    private static boolean inRange(int row, int col, int n) {
        return (0 <= row && row < n) && (0 <= col && col < n);
    }

    private static void init(int n, int k) {
        if (k <= n) {
            x = -1;
            y = k - 1;
            dir = 0;
        } else if (k <= 2 * n) {
            x = (k - n - 1);
            y = n;
            dir = 1;
        } else if (k <= 3 * n) {
            x = n;
            y = n - (k - 2 * n);
            dir = 2;
        } else {
            x = n - (k - 3 * n);
            y = -1;
            dir = 3;
        }
    }

}