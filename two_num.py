# links
# https://leetcode.com/problems/two-sum/submissions/884511113/
def twoNums(n,target):
    complementMap=dict()
    for i,num in enumerate(n): # 4
        complement=target-num  # 2
        if complement not in complementMap:
            complementMap[num]=i # h[3]=0 h[2]=1
        else:
            return [complementMap[complement], i]

n=[5,7,6,8,5]
target=15
print(twoNums(n,target))