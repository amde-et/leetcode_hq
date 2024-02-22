class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1: return ""
        n, m = len(palindrome)-1, len(palindrome)
        while n>=0 and palindrome[n] == "a": n-=1
        if n >= 0 and (m%2==0 or n!=m//2):
            palindrome = palindrome[:m-n-1]+"a"+palindrome[m-n:]
        else:
            palindrome = palindrome[:m-1]+"b"
        return palindrome