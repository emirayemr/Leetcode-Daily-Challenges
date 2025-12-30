class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int R = (int)grid.size();
        int C = (int)grid[0].size();
        if (R < 3 || C < 3) return 0;

        auto isMagic = [&](int r, int c) -> bool {
            // distinct 1..9 check
            bool seen[10] = {false};
            for (int i = r; i < r + 3; i++) {
                for (int j = c; j < c + 3; j++) {
                    int v = grid[i][j];
                    if (v < 1 || v > 9) return false;
                    if (seen[v]) return false;
                    seen[v] = true;
                }
            }

            // For 1..9 3x3 magic square, center must be 5 (optional strong prune)
            if (grid[r + 1][c + 1] != 5) return false;

            // sum checks (must all be 15)
            int s1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2];
            int s2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2];
            int s3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2];
            if (s1 != 15 || s2 != 15 || s3 != 15) return false;

            int t1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c];
            int t2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1];
            int t3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2];
            if (t1 != 15 || t2 != 15 || t3 != 15) return false;

            int d1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2];
            int d2 = grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c];
            if (d1 != 15 || d2 != 15) return false;

            return true;
        };

        int ans = 0;
        for (int i = 0; i + 2 < R; i++) {
            for (int j = 0; j + 2 < C; j++) {
                if (isMagic(i, j)) ans++;
            }
        }
        return ans;
    }
};
