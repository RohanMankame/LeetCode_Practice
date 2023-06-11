class Solution:
    def romanToInt(self, s: str) -> int:

        Ans = 0
        Sarr = [*s]  # split string into str array by char

        # funmction checks curr element and previous element to add and subtract from total ans
        for x in range(0, len(Sarr)):
            if Sarr[x] == "I":
                Ans = Ans + 1

            if Sarr[x] == "V":
                if Sarr[x - 1] == "I" and x != 0:
                    Ans = Ans - 2  # subtract double as we also added it previously if it was earlier in array
                Ans = Ans + 5  # add value of the case

            if Sarr[x] == "X":
                if Sarr[x - 1] == "I" and x != 0:
                    Ans = Ans - 2
                Ans = Ans + 10

            if Sarr[x] == "L":
                if Sarr[x - 1] == "X" and x != 0:
                    Ans = Ans - 20
                Ans = Ans + 50

            if Sarr[x] == "C":
                if Sarr[x - 1] == "X" and x != 0:
                    Ans = Ans - 20
                Ans = Ans + 100

            if Sarr[x] == "D":
                if Sarr[x - 1] == "C" and x != 0:
                    Ans = Ans - 200
                Ans = Ans + 500

            if Sarr[x] == "M":
                if Sarr[x - 1] == "C" and x != 0:
                    Ans = Ans - 200
                Ans = Ans + 1000

        return Ans  # return total calculated

