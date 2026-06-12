class Solution {
public:
    static const int MOD = 1e9 + 7;
    
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        
        vector<vector<int>> g(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        
        int LOG = 17;
        while ((1 << LOG) <= n) LOG++;
        
        vector<int> depth(n + 1, 0);
        vector<vector<int>> up(LOG, vector<int>(n + 1, 0));
        
        queue<int> q;
        q.push(1);
        vector<int> vis(n + 1, 0);
        vis[1] = 1;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v : g[u]) {
                if (!vis[v]) {
                    vis[v] = 1;
                    depth[v] = depth[u] + 1;
                    up[0][v] = u;
                    q.push(v);
                }
            }
        }
        
        for (int j = 1; j < LOG; j++) {
            for (int i = 1; i <= n; i++) {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }
        
        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) swap(a, b);
            
            int diff = depth[a] - depth[b];
            for (int j = 0; j < LOG; j++) {
                if (diff & (1 << j)) a = up[j][a];
            }
            
            if (a == b) return a;
            
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[j][a] != up[j][b]) {
                    a = up[j][a];
                    b = up[j][b];
                }
            }
            
            return up[0][a];
        };
        
        int maxLen = n;
        vector<long long> pow2(maxLen + 1, 1);
        for (int i = 1; i <= maxLen; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        
        vector<int> ans;
        
        for (auto &qr : queries) {
            int u = qr[0], v = qr[1];
            
            int p = lca(u, v);
            int len = depth[u] + depth[v] - 2 * depth[p];
            
            if (len == 0) {
                ans.push_back(0);
            } else {
                ans.push_back((int)pow2[len - 1]);
            }
        }
        
        return ans;
    }
};