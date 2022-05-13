class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def Char_Counter(word):
            whatever = defaultdict(int)
            for i in word:
                whatever[i] += 1
            return whatever
        
        ran = Char_Counter(ransomNote)
        mag = Char_Counter(magazine)
        
        for i in ran:
            if ran[i] > mag[i]:
                return False
        return True