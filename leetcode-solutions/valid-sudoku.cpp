#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        for (auto& row : board) {
            unordered_set<char> cells;
            for (char cell : row) {
                if (cell != '.' && cells.count(cell)) {
                    return false;
                }
                cells.insert(cell);
            }
        }

        for (int col = 0; col < 9; ++col) {
            unordered_set<char> cells;
            for (int row = 0; row < 9; ++row) {
                if (board[row][col] != '.' && cells.count(board[row][col])) {
                    return false;
                }
                cells.insert(board[row][col]);
            }
        }

        for (int rows = 0; rows < 9; rows += 3) {
            for (int cols = 0; cols < 9; cols += 3) {
                unordered_set<char> cells;
                for (int row = rows; row < rows + 3; ++row) {
                    for (int col = cols; col < cols + 3; ++col) {
                        if (board[row][col] != '.' && cells.count(board[row][col])) {
                            return false;
                        }
                        cells.insert(board[row][col]);
                    }
                }
            }
        }

        return true;
    }
};
