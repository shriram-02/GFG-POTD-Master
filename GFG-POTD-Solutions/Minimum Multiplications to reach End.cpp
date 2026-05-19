class Solution {
  public:
    int minSteps(vector<int>& arr, int start, int end) {
        if(start == end)
            return 0;
        
        vector<int> vis(1000, 0);
        queue<pair<int, int>> q;
        
        q.push({start, 0});
        vis[start] = 1;
        
        while(!q.empty()) {
            auto it = q.front();
            q.pop();
            
            int num = it.first;
            int steps = it.second;
            
            for(int x : arr) {
                int nxt = (num * x) % 1000;
                
                if(!vis[nxt]) {
                    if(nxt == end)
                        return steps + 1;
                    
                    vis[nxt] = 1;
                    q.push({nxt, steps + 1});
                }
            }
        }
        
        return -1;
    }
};