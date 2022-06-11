class Solution:
    def sortSentence(self, s: str) -> str:
        splited_s=s.split(" ")
        final_sent=""
        for i in range(len(splited_s)):
            min_index=i
            for j in range(i+1,len(splited_s)):
                if splited_s[j][-1]<splited_s[min_index][-1]:
                    min_index=j
            if i!=min_index:
                splited_s[min_index],splited_s[i]=splited_s[i],splited_s[min_index]
            final_sent += splited_s[i][:-1]+ ' '
        return(final_sent[:-1])
                    
