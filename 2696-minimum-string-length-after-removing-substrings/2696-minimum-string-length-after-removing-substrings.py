class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>=2 and stack[-2:]==['A','B']:
                stack.pop()
                stack.pop()
            if len(stack)>=2 and stack[-2:]==['C','D']:
                stack.pop()
                stack.pop()
        return len(stack)
                
                
            