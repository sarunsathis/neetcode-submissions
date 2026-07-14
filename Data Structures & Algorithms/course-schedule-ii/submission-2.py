class Solution:

    def courseOrder(self,course) :
        if course in self.completionOrder :
            return True
        elif course in self.visiting :
            return False
        elif course not in self.courseMap.keys() or len(self.courseMap[course]) <= 0 :
            self.completionOrder.append(course)
            return True

        self.visiting.add(course)
        for preCourse in self.courseMap[course] :
            if not self.courseOrder(preCourse) :
                return False
        
        self.visiting.remove(course)
        self.completionOrder.append(course)
        return True


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites is None : return []

        self.courseMap = defaultdict(list)
        self.visiting = set()
        self.completionOrder = []

        for ele in prerequisites :
            self.courseMap[ele[0]].append(ele[1])

        for course in range(numCourses) :
            if course in self.courseMap.keys() :
                if not self.courseOrder(course) :
                    return []
            elif course not in self.completionOrder :
                self.completionOrder.append(course)

        return list(self.completionOrder)