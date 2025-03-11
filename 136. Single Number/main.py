def singleNumber1(nums:list)->int:
    results=[]
    for i in nums:
        if(i in results):
            results.remove(i)
        else:
            results.append(i)
        
    return [*results]

def singleNumber2(nums:list)->int:
    results=0
    for i in nums:
        results^=i
    return results

nums=[4,1,2,1,2]
print(singleNumber1(nums))
print(singleNumber2(nums))