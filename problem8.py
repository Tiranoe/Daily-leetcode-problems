# def twosum(nums, target):     
#     arr = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 arr.append(i)
#                 arr.append(j)
#                 print(arr)
#         return arr


def twosum(nums, target): 
    hashnest = {n: i for i, n in enumerate(nums)}
    for i in range(len(nums)):
        n = nums[i]
        complement = target - n
        if complement in hashnest and hashnest[complement] != 1:
            print([hashnest[complement], i])


twosum([3,2,4], 6)