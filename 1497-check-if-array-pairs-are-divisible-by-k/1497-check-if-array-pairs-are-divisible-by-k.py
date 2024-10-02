class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        pair= len(arr)/2
        frqReminder = [0 for _ in range(k)]
        for i in arr:
            rem = i%k
            if(rem<0):
                rem+=k
            frqReminder[rem] +=1
        
        for i in range(1,k-1):
            if frqReminder[i]!=frqReminder[k-i]:
                return False
        
        if frqReminder[0]%2 !=0:
            return False
        return True



        