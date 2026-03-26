class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        const long long MOD = 1e9 + 7;
        
        vector<vector<long long>> maxDp(m, vector<long long>(n));
        vector<vector<long long>> minDp(m, vector<long long>(n));
        
        maxDp[0][0] = minDp[0][0] = grid[0][0];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                
                long long mx = LLONG_MIN, mn = LLONG_MAX;
                
                if (i > 0) {
                    long long a = maxDp[i-1][j] * grid[i][j];
                    long long b = minDp[i-1][j] * grid[i][j];
                    mx = max(mx, max(a, b));
                    mn = min(mn, min(a, b));
                }
                
                if (j > 0) {
                    long long a = maxDp[i][j-1] * grid[i][j];
                    long long b = minDp[i][j-1] * grid[i][j];
                    mx = max(mx, max(a, b));
                    mn = min(mn, min(a, b));
                }
                
                maxDp[i][j] = mx;
                minDp[i][j] = mn;
            }
        }
        
        long long res = maxDp[m-1][n-1];
        if (res < 0) return -1;
        return res % MOD;
    }
};