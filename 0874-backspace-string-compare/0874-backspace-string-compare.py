class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(input_str):
            result = []
            for letter in input_str:
                if letter != '#':
                    result.append(letter)
                elif result:
                    result.pop()
            return ''.join(result)
    
        return build_string(s) == build_string(t)
