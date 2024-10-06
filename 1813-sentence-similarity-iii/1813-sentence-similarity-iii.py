class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        word1 , word2 = sentence1.split(" "),sentence2.split(" ")
        if len(word1)>len(word2):
            word1,word2 = word2,word1
            
        l1=0
        while l1<len(word1) and word1[l1]==word2[l1]:
            l1+=1
        r1,r2=len(word1)-1,len(word2)-1
        while r1>=l1 and r2>=0 and word1[r1]==word2[r2]:
            r1,r2=r1-1,r2-1
        return r1<l1
            