import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;

    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        int[] hs = new int[hFences.length + 2];
        int[] vs = new int[vFences.length + 2];

        hs[0] = 1;
        hs[hs.length - 1] = m;
        for (int i = 0; i < hFences.length; i++) hs[i + 1] = hFences[i];

        vs[0] = 1;
        vs[vs.length - 1] = n;
        for (int i = 0; i < vFences.length; i++) vs[i + 1] = vFences[i];

        Arrays.sort(hs);
        Arrays.sort(vs);

        // All possible heights after removing some horizontal fences = all pairwise differences in hs.
        HashSet<Integer> heights = new HashSet<>();
        for (int i = 0; i < hs.length; i++) {
            for (int j = i + 1; j < hs.length; j++) {
                heights.add(hs[j] - hs[i]);
            }
        }

        int bestSide = 0;
        // Check all possible widths; if also possible as a height, we can form a square of that side.
        for (int i = 0; i < vs.length; i++) {
            for (int j = i + 1; j < vs.length; j++) {
                int w = vs[j] - vs[i];
                if (w > bestSide && heights.contains(w)) bestSide = w;
            }
        }

        if (bestSide == 0) return -1;

        long s = bestSide;
        return (int) ((s % MOD) * (s % MOD) % MOD);
    }
}
