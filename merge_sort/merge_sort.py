def merge_sort(nums):
    if len(nums) != 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        # print([nums, mid, left, right])
        
        left_i = right_i = i = 0
        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                nums[i] = left[left_i]
                left_i = left_i + 1
                i += 1
            else:
                nums[i] = right[right_i]
                right_i = right_i + 1
                i += 1
        while left_i < len(left):
            nums[i] = left[left_i]
            left_i = left_i + 1
            i += 1
        while right_i < len(right):
            nums[i] = right[right_i]
            right_i = right_i + 1
            i += 1
    return nums
        
nums = [0, 3, 1, 7, 6, 8, 2, 4, 9, 5]
result = merge_sort(nums)
print(result)
