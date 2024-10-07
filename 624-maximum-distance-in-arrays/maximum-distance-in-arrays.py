class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays:
            return 0

        m1 = float('inf')
        m2 = float('-inf')
        p1 = float('inf')
        p2 = float('-inf')
        i1 = -1
        i2 = -1

        for i,array in enumerate(arrays):
            f = array[0]
            l = array[-1]

            if f < m1:
                p1,m1 = m1,f
                i1 = i
            elif f < p1:
                p1 = f
            
            if l > m2:
                p2,m2 = m2,l
                i2 = i
            elif l > p2:
                p2 = l

        if i1!=i2:
            return m2-m1
        else:
            return max(m2-p1,p2-m1)

with open('user.out','w') as f:
    for case in map(loads,stdin):
        f.write(f'{Solution().maxDistance(case)}\n')
exit(0)