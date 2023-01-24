# links
# https://leetcode.com/problems/roman-to-integer/
def romantoInteger(text):
    dic={
        "I" :   1,
        "V" :   5,
        "X" :   10,
        "L" :   50,
        "C" :   100,
        "D" :   500,
        "M" :   1000,
    }
    sum=0
    for i in range(len(text)):
        left=i
        right=i+1
        if  right < len(text) and dic[text[left]]< dic[text[right]]:
            value=abs(dic[text[left]]-dic[text[right]])
            sum-=dic[text[i]]
        else:
            sum+=dic[text[i]]
    return sum

print(romantoInteger("III"))