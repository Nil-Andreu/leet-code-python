from typing import List

"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_alist = []

        for idx in range(1, n+1):
            # In the case is divisible by 5
            if idx % 5 == 0:
                # If also divisible by 3
                if idx % 3 == 0:
                    str_alist.append("FizzBuzz")
                else:
                    str_alist.append("Buzz")

            elif idx % 3 == 0:
                str_alist.append('Fizz')
            
            else:
                # Append it as string of the numerical value
                str_alist.append(str(idx))
        
        return str_alist