class Solution {
public:
    int toMinute(const std::string& time) {
        int minutes = 0;
        std::stringstream ss(time);
        std::string token;

        getline(ss, token, ':');
        minutes += stoi(token) * 60;

        getline(ss, token, ':');
        minutes += stoi(token);

        return minutes;
    }

    int findMinDifference(vector<string>& timePoints) {
        
        vector<int> minutes;
        for(auto time : timePoints){
            minutes.push_back(toMinute(time));
        }

        sort(minutes.begin(),minutes.end());
        int length = minutes.size();
        int minMin = minutes[0] , maxMin = 0, ans = 1440;

        for(int i=1; i<length; i++){
            ans = min(ans,minutes[i]-minutes[i-1]);
            minMin = min(minMin, minutes[i]);
            maxMin = max(maxMin, minutes[i]);
        }

        ans = min(ans, 1440 - maxMin + minMin);
        return ans;
    }
};