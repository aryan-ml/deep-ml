import math

def binomial_probability(n: int, k: int, p: float) -> float:
    
    #formula --> nCk * p**k * q**n-k


    c = math.comb(n,k)
    q = 1 - p
    t = n - k

    ans = c * math.pow(p,k) * math.pow(q,t)
    
    return ans
