class Solution:
    def matrixReshape(self, m, r, c):
        flat = [x for row in m for x in row]
        if len(flat) != r * c:
            return m
        return [flat[i*c:(i+1)*c] for i in range(r)]
