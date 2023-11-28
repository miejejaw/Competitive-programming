#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int Top = 0;
        int Right = matrix[0].size() - 1;
        int Bottom = matrix.size() - 1;
        int Left = 0;

        vector<int> result;

        while (true) {
            for (int i = Left; i <= Right; ++i) {
                result.push_back(matrix[Top][i]);
            }
            if (Bottom == Top) {
                break;
            }
            Top += 1;

            for (int i = Top; i <= Bottom; ++i) {
                result.push_back(matrix[i][Right]);
            }
            if (Right == Left) {
                break;
            }
            Right -= 1;

            for (int i = Right; i >= Left; --i) {
                result.push_back(matrix[Bottom][i]);
            }
            if (Top == Bottom) {
                break;
            }
            Bottom -= 1;

            for (int i = Bottom; i >= Top; --i) {
                result.push_back(matrix[i][Left]);
            }
            if (Right == Left) {
                break;
            }
            Left += 1;
        }

        return result;
    }
};
