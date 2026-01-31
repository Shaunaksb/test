def twoSum(nums, target):
    seen={}
    for i, val in enumerate(nums):
        rem = target - val
        if rem in seen:
            return i, seen[rem]
        else:
            seen[val]=i

print(twoSum([3,4,2],6))