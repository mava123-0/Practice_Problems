class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = {}
        for x in words:
            if(x not in ans):
                ans[x] = words.count(x)
        print(ans)
        res = sorted(ans, key=lambda x: (-ans[x], x))
        return res[:k]