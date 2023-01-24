
# link:
# https://leetcode.com/problems/palindrome-number/
def isPalindrome(x):
    lx=list(str(x))
    rev=lx[::-1]
    if lx==rev:
        return True
    else:
        return False
    
    
x=121
print(isPalindrome(x))