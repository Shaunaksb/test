def subset(nums):
    res=[]
    n=len(nums)
    for i in range(1 << n):
        sbset=[]
        for j in range(n):
                if i & (1 << j):
                    sbset.append(nums[j])
        res.append(sum(sbset))
    return(res)

print(subset([1,2,3,4]))