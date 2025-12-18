// 11399 ATM
// 읽기 : BufferedReader

import java.io.*;
import java.util.*;

public class java_11399_ATM {
    public static void main(String[] args) throws Exception {
        
        // ATM 앞에 N명의 사람들이 줄을 서있다
        // i번째 사람이 돈을 인출하는데 걸리는 시간은 pi분
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));        
        int N = Integer.parseInt(br.readLine());

        // 한줄을 받아 ArrayList로 변환
        int[] p = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            p[i] = Integer.parseInt(st.nextToken());
        }

        // 각 사람이 돈을 인출하는데 필요한 시간의 합 최소
        // 정렬을 오름차순으로 하고, 피보나치 수열로 누적합을 구한다.
        Arrays.sort(p);

        int prefix = 0; // 지금까지 누적(대기+인출)
        int total = 0;  // 모든 사람의 합
        for (int i = 0; i < N; i++) {
            prefix += p[i];
            total += prefix;
        }

        System.out.println(total);
    }
}
