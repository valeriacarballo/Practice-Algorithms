# 0f(n) = n*n (quadratic time)
def twoSum(nums, target):
    for p1 in range(len(nums)):
        for p2 in range(len(nums)):
            y = p2 + 1
            if y >= len(nums):
                break
            if y == p1:
                continue
            if nums[p1] + nums[y] == target:
                return [p1, y]
   

nums = [1, 6, 7, 4, 9]
print(twoSum(nums, 10))


