class DetectSquares {
public:
    unordered_map<int,unordered_set<int>> vertical;
    vector<vector<int>> grid;

    DetectSquares() {
        grid.resize(1001, vector<int>(1001, 0));
    }
    
    void add(vector<int> point) {
        vertical[point[1]].insert(point[0]);
        grid[point[0]][point[1]] += 1;
    }
    
    int count(vector<int> point) {
        int count = 0;
        int a=point[0],b=point[1];

        for(int x : vertical[b]){
            if(x == a) continue;
            int d = abs(a-x);
            if(b+d < 1001){
                count += grid[x][b] * grid[a][b+d] * grid[x][b+d];
            }

            if(b-d >= 0){
                count += grid[x][b] * grid[a][b-d] * grid[x][b-d];
            }
        }

        return count;
    }
};
