class Solution:
    def imageSmoother(self, img):
        R, C = len(img), len(img[0])
        res = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                s = n = 0
                for dr in (-1,0,1):
                    for dc in (-1,0,1):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C:
                            s += img[nr][nc]; n += 1
                res[r][c] = s // n
        return res
