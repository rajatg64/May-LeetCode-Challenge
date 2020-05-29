class Solution:
    def addEdge(self,graph, src, dest):
        if graph[src] is None:
            graph[src] = [dest]
        else:
            graph[src].append(dest)
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [None] * numCourses    
        for i in range(len(prerequisites)):
            self.addEdge(graph,prerequisites[i][0],prerequisites[i][1])
        #print(graph)
        inDegree = [0] * len(graph) 
        for i in range(len(graph)):
            temp = graph[i]
            if temp is not None:
                for j in range(len(temp)):
                    inDegree[temp[j]] += 1
        q = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
        res = []
        while q:
            temp = q.pop(0)
            res.append(temp)
            g = graph[temp]
            if g is not None:
                for i in range(len(g)):
                    inDegree[g[i]] -= 1
                    if inDegree[g[i]] == 0:
                        q.append(g[i])
                    
        if len(res) == numCourses:
            return True
        else:
            return False
            
            
                