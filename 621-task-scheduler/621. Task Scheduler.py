from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        max_heap = [-freq for freq in dic.values()]
        heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            idle = n + 1
            while idle > 0 and max_heap:
                freq = -heappop(max_heap)
                temp.append(freq - 1)
                idle -= 1
                time += 1
            for freq in temp:
                if freq > 0:
                    heappush(max_heap, -freq)
            if not max_heap:
                break
            time += idle if idle > 0 else 0
        return time

        arr = []
        for key in dic:
            arr.append(dic[key])
        arr.sort(reverse=True)
        time = 0
        while sum(arr) != 0:
            idle = n
            for i in range(len(arr)):
                if arr[i] != 0:
                    arr[i] -= 1
                    time += 1
                    idle -= 1 if i != 0 else 0
                    if idle == 0:
                        break
            if sum(arr) == 0:
                break
            if idle > 0:
                time += idle
        return time