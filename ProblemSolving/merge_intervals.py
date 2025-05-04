# 56. Merge Intervals

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals_map = {}
        for i in intervals:
            if i[0] in intervals_map.keys():
                intervals_map[i[0]] = max(i[1],intervals_map[i[0]])
            else:
                intervals_map[i[0]] = i[1]
        keys = sorted(list(intervals_map.keys()))
        
        output = []

        s,e = keys[0],intervals_map[keys[0]]
        for i in keys:
            if i <= e:
                e = max(e, intervals_map[i])
            else:
                output.append([s,e])
                s,e = i,intervals_map[i]
        output.append([s,e])
        return output

print(merge([[1,3],[2,6],[8,10],[15,18]]))