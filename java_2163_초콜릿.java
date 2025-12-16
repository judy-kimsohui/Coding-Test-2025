// 2163 초콜릿

// N * M 크기의 초콜릿
// 초콜릿을 쪼개는 횟수를 최소

// 긴쪽으로 먼저 자르고, 짧은 쪽을 자른다

// 읽기 : BufferedReader
// 출력 : BufferedWriter

import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        System.out.println(N * M - 1);
    }
}
