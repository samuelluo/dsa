// g++ -std=c++17 merge_sort.cpp
// Includes
#include <algorithm>    // std::shuffle
#include <iostream>     // std::cout, std::endl
#include <random>       // std::random_device
#include <vector>       // std::vector

// Globals
std::random_device rd;

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
    // Shuffle vector of 1 to 10
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::shuffle(std::begin(nums), std::end(nums), rd);
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
