class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses             # Count incoming edges for each course
        adj = [[] for i in range(numCourses)]   # Adjacency list
        
        # Build graph and calculate indegrees
        for src, dst in prerequisites:
            indegree[dst] += 1                  # dst has one more prerequisite
            adj[src].append(dst)                # src points to dst
        
        # Find all courses with no prerequisites (indegree = 0)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)                     # Can take these courses immediately
        
        finish = 0                              # Count completed courses
        while q:                                # Process courses level by level
            node = q.popleft()                  # Take a course with no prerequisites
            finish += 1                         # Mark as completed
            
            for nei in adj[node]:               # For each course that depends on this one
                indegree[nei] -= 1              # Remove this prerequisite
                if indegree[nei] == 0:          # If all prerequisites satisfied
                    q.append(nei)               # Can now take this course
                
        return finish == numCourses             # Did we complete all courses?
