class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        SarrHayS = [*haystack]
        SarrNeed = [*needle]

        print(SarrHayS)
        print(SarrNeed)
        xPoCount = int(len(SarrNeed) - 1)
        xPo = []
        firstChar = SarrNeed[0]

        for x in range(0, len(SarrHayS)):
            if SarrHayS[x] == firstChar:
                for (y, z) in zip(SarrHayS, SarrNeed):
                    if (y == z) is True:
                        print(y, z)
                        xPo.append(x)

        if (xPoCount < len(xPo)) and (xPo[xPoCount] == xPo[0]):
            return xPo[0]
        else:
            return -1