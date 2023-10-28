class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        
        int years[101] = {0};
        for(auto year : logs){
            years[year[0]-1950] += 1;
            years[year[1]-1950] -= 1;
        }

        int year=0,total=0,max_popu=0;
        for (int i=0; i<100; i++) {
            total += years[i];
            if (total > max_popu) {
                max_popu = total;
                year = i;
            }
        }
        return year+1950;
    }
};