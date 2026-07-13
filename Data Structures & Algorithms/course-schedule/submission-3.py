class Solution:

    def dfs(self,course) :
        if (course not in self.courseMap.keys()) or len(self.courseMap[course]) <= 0 :
            self.completed.append(course)
            return True
        elif course in self.completed :
            return True
        elif course in self.visiting :
            return False

        self.visiting.append(course)
        for preCourse in self.courseMap[course] :
            if not self.dfs(preCourse) :
                return False
        
        self.visiting.remove(course)
        self.completed.append(course)
        
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites is None or len(prerequisites) == 0 :
            return True

        self.courseMap = defaultdict(list)
        self.visiting = []
        self.completed = []

        for ele in prerequisites :
           self.courseMap[ele[0]].append(ele[1])

        for ele in self.courseMap.keys() :
            if not self.dfs(ele) :
                return False

        return True