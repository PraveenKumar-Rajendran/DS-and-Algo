class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me
# https://www.youtube.com/watch?v=HsBefuOqkd4
        
        def dfs(rank, curr, prev):
            low[curr] = rank
            for neighbor in edges[curr]:
                if neighbor == prev: continue
                if not low[neighbor]:
                    dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    result.append([curr, neighbor])
        
        
        low, edges, result = [0] * n, collections.defaultdict(list), []
        for u, v in connections: 
            edges[u].append(v)
            edges[v].append(u)
            
        dfs(1, 0, -1)
        return result