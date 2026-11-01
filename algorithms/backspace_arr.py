class Solution:
    def solution(self, s, t):
        res_string1 = self.helper(s)
        res_string2 = self.helper(t)

        if res_string1 == res_string2:
            print(True)
        else:
            print(False)


    def helper(self, givenstr):
        res_arr = []
        for i in givenstr:
            if i != "#":
                res_arr += i
            else:
                res_arr.pop()

        res_string = ''.join(res_arr)
        return res_string


