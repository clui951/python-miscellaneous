class Solution(object):
    # Use a nested function to help generate valid permutations
    # break up n into a counter for open parens and close parens
    # counters determine what char can be put next
    # have a nonlocal result which is manipulated in place by DFS / backtracking
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results_list = []
        result = [0] * 2 * n

        def generate_results(left, right):
            nonlocal results_list
            nonlocal result

            if left == right == 0:
                results_list.append("".join(result))
                return
            
            position = 2 * n - left - right
            if left > 0:
                result[position] = "("
                generate_results(left - 1, right)
            if right > 0 and right > left:
                result[position] = ")"
                generate_results(left, right - 1)

        generate_results(n,n)
        return results_list

        


if __name__ == "__main__":
    print("=== generateParenthesis ===")

    expected = set([
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ])
    actual = set(Solution().generateParenthesis(3))
    print(actual)
    assert actual == expected

    print("=== done! ===")