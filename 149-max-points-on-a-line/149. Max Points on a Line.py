class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3: return len(points)


        res = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                point1x, point1y = points[i][0], points[i][1]
                points2x, points2y = points[j][0], points[j][1]
            
                dy, dx = points2y - point1y, points2x - point1x
                samePoints = 0
                if dy == 0 and dx == 0:
                    samePoints+=1
                elif dx == 0:
                    dic["inf"] = 1 + dic.get("inf", 0)
                else:
                    slope = dy / dx
                    dic[slope] = 1 + dic.get(slope, 0)
                
                res = max(res, samePoints)
                for slope, count in dic.items():
                    res = max(res, samePoints + count)
        return res




        