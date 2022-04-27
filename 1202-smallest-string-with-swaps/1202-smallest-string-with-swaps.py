class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visited.add(i)
            tmp.append(s[i])
            idx.append(i)
            for j in d[i]:
                if j not in visited:
                    dfs(j)

        if not pairs or not pairs[0]:
            return s
        
        lst = list(s)
        visited = set()
        d = [[] for _ in range(len(s))]
        for i, j in pairs:
            d[i].append(j)
            d[j].append(i)
        
        for i in range(len(s)):
            if i not in visited:
                tmp = []
                idx = []
                dfs(i)
                tmp = sorted(tmp)
                idx = sorted(idx)
                for index in range(len(idx)):
                    lst[idx[index]] = tmp[index]
        
        return ''.join(lst)