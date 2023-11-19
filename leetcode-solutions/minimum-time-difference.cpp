class Solution {
public:
    int toMinute(const std::string& time) {
        int hours = stoi(time.substr(0,2));
        int mins = stoi(time.substr(3,2));
        int minutes = hours*60 + mins;

        return minutes;
    }

    int findMinDifference(vector<string>& timePoints) {
        
        vector<int> minutes;
        for(auto time : timePoints){
            minutes.push_back(toMinute(time));
        }

        sort(minutes.begin(),minutes.end());
        int length = minutes.size();
        int ans = 1440;

        for(int i=1; i<length; i++){
            ans = min(ans,minutes[i]-minutes[i-1]);
        }

        ans = min(ans, 1440 + minutes[0] - minutes[length-1]);
        return ans;
    }
};