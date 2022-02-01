# -*- coding: UTF-8 -*-
'''
@Project ：week13 
@File ：60. Permutation Sequence.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-02 오전 2:33 
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1,n+1)]
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k-=1
        ans = []
        for i in range(n,0,-1):
            id = k//fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            nums.pop(id)
        return "".join(ans)


s = Solution()
print(s.getPermutation(3,3))
