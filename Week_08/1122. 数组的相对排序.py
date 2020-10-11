class Solution:
    def reverseBits(self, n: int) -> int:
        # #bin zfill
        return int( bin(n)[2::].zfill(32)[::-1], base=2)
        # # # 位移
        # # res = 0
        # # for i in range(32):
        # #     res = (res << 1) + (n & 1)
        # #     n >>= 1
        # # return res