from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        output = []
        intervals.sort()

        current = intervals[0]
        output.append(current)

        for i in range(len(intervals)):
            current2 = current[1]
            next1 = intervals[i][0]
            next2 = intervals[i][1]

            if current2 >= next1:
                current[1] = max(current2, next2)
            else:
                current = intervals[i]
                output.append(current)
        print(output)
        return output


Solution.merge(self=Solution, intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
Solution.merge(self=Solution, intervals=[[1, 4], [4, 5]])
