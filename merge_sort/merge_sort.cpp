// g++ -std=c++14 merge_sort.cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <random>

std::vector<int> mergeSort(std::vector<int> nums) {
    if (nums.size() == 1) {
        return nums;
    } else {
        int mid = nums.size()/2;
        std::vector<int> left(&nums[0], &nums[mid]);
        std::vector<int> right(&nums[mid], &nums[nums.size()]);
        left = mergeSort(left);
        right = mergeSort(right);

        int left_i = 0; int right_i = 0; int i = 0;
        while (left_i < left.size() && right_i < right.size()) {
            if (left[left_i] < right[right_i]) {
                nums[i] = left[left_i];
                left_i += 1; i += 1;
            } else {
                nums[i] = right[right_i];
                right_i += 1; i += 1;
            }
        }
        while (left_i < left.size()) {
            nums[i] = left[left_i];
            left_i += 1; i += 1;
        }
        while (right_i < right.size()) {
            nums[i] = right[right_i];
            right_i += 1; i += 1;
        }
    }
    return nums;
}

int main() {
    // Generate random list of 10 numbers
    // std::srand(std::time(0));
    // std::vector<int> nums;
    // for (int i = 0; i < 10; i++) {
    //     int num = rand() % 10 + 1;
    //     nums.push_back(num);
    // }

    // Shuffle vector of 1 to 10
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(std::begin(nums), std::end(nums), g);
    for (auto i : nums) {
        std::cout << i << ' ';
    }
    std::cout << std::endl;

    // Sort
    nums = mergeSort(nums);
    for (auto i : nums) {
        std::cout << i << ' ';
    }
    std::cout << std::endl;
}