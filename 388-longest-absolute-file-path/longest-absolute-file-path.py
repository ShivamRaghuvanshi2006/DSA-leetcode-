class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen=0
        d={-1:0}
        for line in input.split('\n'):
            depth=len(line)-len(line.lstrip('\t'))
            name=line.lstrip('\t')
            if '.' in name:
                maxlen=max(maxlen, d[depth-1]+len(name))
            else:
                d[depth]=d[depth-1]+len(name)+1
        return maxlen