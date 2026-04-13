class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # Standard phone keypad mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # Base case: if the current combination is complete
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # Get letters for the current digit and recurse
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop() # Backtrack to try the next letter
        
        backtrack(0, [])
        return res
