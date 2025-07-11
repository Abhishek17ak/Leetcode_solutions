class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses             # Count prerequisites for each course
        adj = [[] for i in range(numCourses)]   # Adjacency list
        
        # Build graph and calculate indegrees
        for src, dst in prerequisites:
            indegree[dst] += 1                  # dst has one more prerequisite
            adj[src].append(dst)                # src enables dst
        
        # Find courses with no prerequisites
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish, output = 0, []                  # Track completion and store order
        while q:
            node = q.popleft()                  # Take next available course
            output.append(node)                 # Add to our course sequence
            finish += 1                         # Count as completed
            
            for nei in adj[node]:               # For each course this unlocks
                indegree[nei] -= 1              # Remove this prerequisite
                if indegree[nei] == 0:          # All prerequisites satisfied?
                    q.append(nei)               # Can now take this course
        
        if finish != numCourses:                # Couldn't complete all courses?
            return []                           # Impossible (cycle detected)
        return output[::-1]                     # Return reversed order
