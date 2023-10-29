class DetectSquares {
public:
    unordered_map<int,unordered_map<int,int>> points;

    DetectSquares() {

    }
    
    void add(vector<int> point) {
        points[point[1]][point[0]] += 1;
    }
    
    int count(vector<int> point) {
        int count = 0;
        int x=point[0],y=point[1];

        for(auto& p : points[y]){
            if(x == p.first) continue;

            int d = abs(x-p.first);
            if(y+d < 1001){
                count += p.second * points[y+d][x] * points[y+d][p.first];
            }

            if(y-d >= 0){
                count += p.second * points[y-d][x] * points[y-d][p.first];
            }
        }

        return count;
    }
};
