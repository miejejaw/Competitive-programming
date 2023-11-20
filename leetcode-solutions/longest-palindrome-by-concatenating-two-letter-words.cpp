class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> freq;

        for (auto& word : words) {
            freq[word]++;
        }

        int ans = 0;
        bool check = true;

        for (auto& it : freq) {
            if (it.first[0] == it.first[1]) {
                ans += (it.second/2) * 4;

                if(check && it.second%2 == 1){
                    ans += 2;
                    check = false;
                }
            } else {
                string temp = {it.first[1], it.first[0]};
                if(freq.count(temp))
                    ans += min(it.second, freq[temp]) * 2;
            }
        }

        return ans;
    }
};