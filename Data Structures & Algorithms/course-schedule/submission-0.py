class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            degrees[prereq[0]] += 1
            adjlist[prereq[1]].append(prereq[0])
        
        q = deque()

        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)
        
        count = 0

        while not len(q) == 0:
            popped = q.popleft()
            count += 1

            
            for curr in adjlist[popped]:
                degrees[curr] -= 1
                if degrees[curr] == 0:
                    q.append(curr)
        return count == numCourses

        
        