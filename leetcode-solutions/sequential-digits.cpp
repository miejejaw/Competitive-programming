class Solution {
public:
    std::vector<int> sequentialDigits(int low, int high) {
        std::vector<int> result;
        int currentNumLength = std::log10(low) + 1;
        int currentNum = initialize(currentNumLength);
        int addValue = 0;

        for (int i = 0; i < currentNumLength; i++) {
            addValue = addValue * 10 + 1;
        }

        while (currentNum <= high) {
            if (low <= currentNum && currentNum <= high) {
                result.push_back(currentNum);
            }

            if (currentNum % 10 == 9) {
                currentNumLength++;
                currentNum = initialize(currentNumLength);
                addValue = addValue * 10 + 1;
            } else {
                currentNum += addValue;
            }
        }
        return result;
    }

    int initialize(int length) {
        int num = 1;
        for (int i = 1; i < length; i++) {
            num = num * 10 + num % 10 + 1;
        }
        return num;
    }
};