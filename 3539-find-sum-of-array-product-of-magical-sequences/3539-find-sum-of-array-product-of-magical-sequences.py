class Solution:
    def magicalSum(self, m: int, k: int, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations
        C = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            C[i][0] = C[i][i] = 1
            for j in range(1,i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        # Precompute powers
        pow_nums = [[1]*(m+1) for _ in range(n)]
        for i in range(n):
            for j in range(1,m+1):
                pow_nums[i][j] = pow_nums[i][j-1] * nums[i] % MOD

        from collections import defaultdict
        dp = {(0,0,0):1}  # used, carry, bits

        for i in range(n):
            new = defaultdict(int)

            for (used, carry, bits), val in dp.items():

                for take in range(m-used+1):

                    ways = C[m-used][take]
                    prod = pow_nums[i][take]

                    s = carry + take
                    new_bits = bits + (s & 1)
                    new_carry = s >> 1

                    if new_bits > k:
                        continue

                    new[(used+take, new_carry, new_bits)] = (
                        new[(used+take, new_carry, new_bits)]
                        + val * prod % MOD * ways
                    ) % MOD

            dp = new

        ans = 0

        for (used, carry, bits), val in dp.items():
            if used == m:
                total_bits = bits + bin(carry).count("1")
                if total_bits == k:
                    ans = (ans + val) % MOD

        return ans