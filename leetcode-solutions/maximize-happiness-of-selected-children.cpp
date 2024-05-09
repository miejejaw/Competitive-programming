template<typename T>
struct Greater {
    bool operator()(const T& a, const T& b) const {
        return a > b;
    }
};

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        
        sort(happiness.begin(), happiness.end(),  [](long long a, long long b) {
            return a > b;
        });

        long long total = 0;
        for(int i=0; i<k; i++){
            if(happiness[i] <= i) break;
            total += happiness[i]-i;
        }

        return total;
    }
};