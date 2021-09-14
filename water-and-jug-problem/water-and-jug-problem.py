class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        q = collections.deque([(0, 0)])
        visited = set([(0,0)])
        step = 0
        while q :
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                jug1, jug2 = node
                if jug1 == targetCapacity or jug2 == targetCapacity or jug1 + jug2 == targetCapacity:
                    return True

                if jug1 and (0, jug2) not in visited:
                    q.append((0, jug2))
                    visited.add((0, jug2))

                if jug2 and (jug1, 0) not in visited:
                    q.append((jug1, 0))
                    visited.add((jug1, 0))

                if jug1 < jug1Capacity and (jug1Capacity, jug2) not in visited:
                    q.append((jug1Capacity, jug2))
                    visited.add((jug1Capacity, jug2))

                if jug2 < jug2Capacity and (jug1, jug2Capacity) not in visited:
                    q.append((jug1, jug2Capacity))
                    visited.add((jug1, jug2Capacity))
                
                val = jug2 - jug1Capacity + jug1
                fill1 = (min(jug1Capacity, jug1 + jug2), min(jug2Capacity, max(0, val)) )
                if jug2 and fill1 not in visited:
                    q.append(fill1)
                    visited.add(fill1)
                    
                val = jug1 - jug2Capacity + jug2
                fill2 = (min(jug1Capacity, max(0, val)), min(jug2Capacity, jug1 + jug2))
                if jug1 and fill2 not in visited:
                    q.append(fill2)
                    visited.add(fill2)
                # print()
                # print(step)
                # print(q)
                # print(visited)
            step += 1
        return False