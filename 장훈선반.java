import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 장훈선반 {

    static int N, B;
    static int[] heights;
    static int best;

    static void dfs(int i, int sum) {
        // 이미 현재 best보다 커졌으면 가지치기
        if (sum >= best) return;

        // B 이상이면 best 갱신
        if (sum >= B) {
            best = Math.min(best, sum);
            return;
        }

        // 끝까지 다 봤으면 종료
        if (i == N) return;

        // i번째 포함
        dfs(i + 1, sum + heights[i]);
        // i번째 미포함
        dfs(i + 1, sum);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());

            heights = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                heights[i] = Integer.parseInt(st.nextToken());
            }

            // 가지치기 성능 향상
            Arrays.sort(heights);
            for (int i = 0; i < N / 2; i++) {
                int tmp = heights[i];
                heights[i] = heights[N - 1 - i];
                heights[N - 1 - i] = tmp;
            }

            best = Integer.MAX_VALUE;
            dfs(0, 0);

            sb.append("#").append(tc).append(" ")
              .append(best - B).append("\n");
        }

        System.out.print(sb);
    }
}
