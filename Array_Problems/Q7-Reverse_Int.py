class Solution:
    def reverse(self, x: int) -> int:

        nArr = [*str(x)]
        L = len(nArr) - 1
        S = ""

        if nArr[0] == "-":
            S = "-"
            for x in range(L, 0, -1):
                S = S + nArr[x]

        else:
            for x in range(L, -1, -1):
                S = S + nArr[x]

        Val = int(S)

        if Val > (2 ** (31)) - 1 or Val < -2 ** (31):
            return 0
        else:
            return Val