from functools import lru_cache
from time import time

class Fibonacci:
    def __init__(self):
        self.cache={0: 0,1: 1} #questo già lo so


    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self, n):
        if self.cache.get(n) is not None:
            return self.cache[n]

        else:
            self.cache[n] = (self.calcola_elemento_lru(n - 1) + self.calcola_elemento_lru(n - 2))

            return self.cache[n]


    def calcola_elemento(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1

        else:
            return (self.calcola_elemento(n-1)+self.calcola_elemento(n-2))



if __name__=="__main__":
    N=40
    fib=Fibonacci()
    start_time=time()
    print(fib.calcola_elemento(N))
    end_time=time()
    print(f"Tempo impiegato: {end_time-start_time}")

    start_time = time()
    print(fib.calcola_elemento_lru(N))
    end_time = time()
    print(f"Tempo impiegato cache: {end_time - start_time}")

