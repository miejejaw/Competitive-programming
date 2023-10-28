class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        
        map<int,int> years;
        for(auto year : logs){
            years[year[0]] += 1;
            years[year[1]] -= 1;
        }

        int year=0,total=0,max_popu=-1;
        for (auto it = years.begin(); it != years.end(); ++it) {
            total += it->second;
            if (total > max_popu) {
                max_popu = total;
                year = it->first;
            }
        }
        return year;
    }
};