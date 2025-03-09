class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.replace(",","").replace(":","").lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        rs="".join(s.split())
        return rs==rs[::-1]