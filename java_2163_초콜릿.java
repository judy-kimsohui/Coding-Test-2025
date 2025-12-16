// 2163 초콜릿

import java.io.*;
import java.util.*;

// N * M 크기의 초콜릿
// 초콜릿을 쪼개는 횟수를 최소

// 긴쪽으로 먼저 자르고, 짧은 쪽을 자른다

// 읽기 : BufferedReader
// 출력 : BufferedWriter

class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tkn = new StringTokenizer(br.readLine());
    
        int N = Integer.parseInt(tkn.nextToken());
        int M = Integer.parseInt(tkn.nextToken());

        // N이 더 긴쪽 : 
        if (N >= M) {
            System.out.println(M * (N-1) + M-1);
        }
        else {
            System.out.println(N * (M-1) + N-1);
        }        
    }
}