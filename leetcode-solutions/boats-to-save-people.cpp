class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {

        sort(people.begin(), people.end());
        int ans = 0;
        for (int l = 0, r = people.size() - 1; l <= r;) {

            if (people[l] + people[r] <= limit) {
                l++;
            }
            
            r--;
            ans++;
        }

        return ans;
    }
};