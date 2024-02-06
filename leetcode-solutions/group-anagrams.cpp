class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> hmap;

        for (const auto& word : strs) {
            string temp = word;
            sort(temp.begin(), temp.end());
            hmap[temp].push_back(word);
        }

        vector<vector<string>> result;

        for (const auto& aa : hmap) {
           result.push_back(aa.second);
        }

        return result;
    }
};