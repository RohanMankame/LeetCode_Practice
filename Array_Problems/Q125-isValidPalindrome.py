class Solution:
    def isPalindrome(self, s: str) -> bool:

        L = []
        Laar = s.lower()
        Test = True

        for x in Laar:
            if (x.isalpha() and x != " ") or x.isnumeric():
                L.append(x)

        print(L)

        FinalP = len(L) - 1

        for i in range(0, len(L) - 1):

            if i >= FinalP:
                break

            if L[i] == L[FinalP]:
                Test = True

            if L[i] != L[FinalP]:
                Test = False
                print(i, FinalP)
                break

            FinalP -= 1

        print(L)

        return Test