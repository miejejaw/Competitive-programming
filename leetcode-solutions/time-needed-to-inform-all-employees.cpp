class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        unordered_map<int, vector<int>> graph;

        for (int emp = 0; emp < n; ++emp) {
            if (emp != headID) {
                graph[manager[emp]].push_back(emp);
            }
        }

        queue<pair<int, int>> q;
        q.push({headID, informTime[headID]});
        int timeTaken = 0;

        while (!q.empty()) {
            auto [curr, t] = q.front();
            q.pop();

            timeTaken = max(timeTaken, t);

            for (int emp : graph[curr]) {
                q.push({emp, t + informTime[emp]});
            }
        }

        return timeTaken;
        
    }
};