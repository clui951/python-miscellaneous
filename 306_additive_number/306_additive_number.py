import itertools
class Solution:
    
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # let i/j be splice index of end of first/second numbers respectively (this is enough to deterministically finish the list)
        # for all combinations of i,j
        #   build out the list and try to see if the given list matches
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]
                if a != str(int(a)) or b != str(int(b)):
                    continue

                while j < n:
                    c = str(int(a) + int(b))
                    if num[j:].startswith(c):
                        j += len(c)
                        a = b
                        b = c
                    else:
                        break
                if j == n:
                    return True
        return False

        # this attempt tried to continuosly check the sum value by iterating down and appending more elements to the last number
        # for i in range(1, len(num) - 1):
        #     for j in range(i + 1, len(num)):
        #         print("i", i, "  j", j)
                
        #         a_string = num[:i]
        #         a = int(a_string)
        #         b_string = num[i:j]
        #         b = int(b_string)
                
        #         # checks for leading 0's
        #         if a_string != str(a):
        #             continue
        #         if b_string != str(b):
        #             continue

        #         s = j + 1
        #         while s < len(num) + 1:
        #             # possible sum value
        #             ss_string = num[j : s]
        #             ss = int(ss_string)
        #             print("     i", i, "  j", j, "  s", s)
        #             print("     a", a, "  b", b, "  ss_string", ss_string)
        #             print("----")
                    
        #             # checks for leading 0's
        #             if ss_string != str(ss):
        #                 break
                    
        #             # stop searching, for sake of efficiency
        #             if ss > a + b:
        #                 break
                    
        #             # successful additive sum found, slide values and to start searching for next
        #             if ss == a + b:
        #                 if s == len(num):
        #                     return True
        #                 a = b
        #                 b = ss
        #                 j = s
        #             s += 1
                
        # return False




if __name__ == "__main__":
    print("=== additive number ===")

    s = Solution()
    assert s.isAdditiveNumber("112358") == True
    print("DONE")
    assert s.isAdditiveNumber("199100199") == True
    print("DONE")
    assert s.isAdditiveNumber("1991001991") == False
    print("DONE")
    assert s.isAdditiveNumber("1991001992") == False
    print("DONE")
    assert s.isAdditiveNumber("123") == True
    print("DONE")
    assert s.isAdditiveNumber("1023") == False

    print("=== done! ===")