class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int i = 1;
        string prefix = "";

        while (strs[0].size() >= i) {
            for (string& s : strs) {
                if (strs[0].substr(0, i) != s.substr(0, i)) {
                    return s.substr(0, i - 1);
                }
            }
            i++;
        }

        return strs[0]; 
    }
};