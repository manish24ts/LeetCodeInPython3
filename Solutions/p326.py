class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n>1): 
            while(n%3==0):
                n//=3
        if n == 1:
            return True
        else:
            return False
'''
Self explanatory
'''
