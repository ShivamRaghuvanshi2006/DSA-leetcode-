class Solution:
    def fizzBuzz(self, n):
        r = []
        for i in range(1, n + 1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            r.append(s or str(i))
        return r
