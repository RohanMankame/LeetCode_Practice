

class Solution(object):
    def lengthOfLastWord(self, s):
        L = len(s)

        Words = s.split(" ")

        LastWordLen = len(Words[-1])

        for x in reversed(Words):
            if x != '':
                LastWord = x
                break

        print(LastWord)
        return len(LastWord)

