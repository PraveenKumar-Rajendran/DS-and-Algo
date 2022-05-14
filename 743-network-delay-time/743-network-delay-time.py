class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's algorithm NTC
        Travel_time = 0
        
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        
        minHeap = [(0,k)] 
        visit = set()
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in visit:
                continue
            visit.add(n1)
            
            Travel_time = max(Travel_time, w1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1 + w2, n2))
                
        return Travel_time if len(visit) == n else -1    
    
#         edges = collections.defaultdict(list)
#         for u, v, w in times:
#             edges[u].append((v, w))
        
#         minHeap = [(0, k)]
#         visit = set()
#         t = 0
#         while minHeap:
#             w1, n1 = heapq.heappop(minHeap)
#             if n1 in visit:
#                 continue
#             visit.add(n1)
#             t = max(t, w1)
            
#             for n2, w2 in edges[n1]:
#                 if n2 not in visit:
#                     heapq.heappush(minHeap, (w1 + w2, n2))
#         return t if len(visit) == n else -1                    