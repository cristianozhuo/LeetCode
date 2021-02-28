class Solution:
    def reverse(self, x: int) -> int:
        if x<0: return -self.reverse(-x)

        n = []
        new_x = 0

        while(x>=10):
            n.append(x%10)
            x=x//10

        n.append(x%10)

        m = len(n)
        for i in range(m):
            new_x = new_x + n[i]*10**(m-i-1)
        
        if new_x<-2**31 or new_x>2**31-1: return 0
        else: return new_x
