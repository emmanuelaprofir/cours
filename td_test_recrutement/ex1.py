"""def two_sum(nums:list[int], cible:int)-> list[int]:
    res = []
    if len(nums)<1:
        return []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == cible:
                res.append(i)
                res.append(j)
                return res"""

def two_sum(nums:list[int], cible:int)-> list[int]:
    
    dico = {elt: cible-elt for elt in nums}
    for i in range(len(nums)-1):
        if nums[i]<cible:
            if nums[i]in dico and cible-nums[i] in dico:
                return [i,nums.index(cible-nums[i])]
    return []


num=[1,4,8,3]
print(two_sum(num,11))


