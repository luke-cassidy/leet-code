import math


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        if n > 2:
            primes.append(2)

        for i in range(3, n, 2):
            if self.isPrime(i):
                primes.append(i)

        return primes

    def isPrime(self, n: int) -> bool:
        if n < 3:
            return False

        # largest 2 possible multiples without repeating are p * q where p=q,
        # since p * q = n, then p & q == sqrt(n)
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True


class Solution2:
    def countPrimes(self, n: int) -> int:
        primes = set()

        if n < 2:
            return 0

        # add all to primes set
        for i in range(2, n):
            primes.add(i)

        # remove non-primes from primes set
        # largest 2 possible multiples without repeating are p * q where p=q,
        # since p * q = n, then p & q == sqrt(n)
        for i in range(2, int(math.sqrt(n)) + 1):
            # if this has already been removed then you can skip, as all multiples
            # of this will be contained in the set of the multiples of the previous
            # items
            if i not in primes:
                continue
            # can start at i * i because up until now i * (i - x),
            # where {x| 0 < x <= i - 1), has been calced
            for j in range(i * i, n, i):
                # check if it has already been removed because
                # it might have been a multiple of a previous j
                primes.discard(j)

        return len(primes)


n = 0
ans = Solution2().countPrimes(n)
print("ans: {}".format(ans))

n = 1
ans = Solution2().countPrimes(n)
print("ans: {}".format(ans))

n = 2
ans = Solution2().countPrimes(n)
print("ans: {}".format(ans))

n = 12
ans = Solution2().countPrimes(n)
print("ans: {}".format(ans))

n = 24
ans = Solution2().countPrimes(n)
print("ans: {}".format(ans))
