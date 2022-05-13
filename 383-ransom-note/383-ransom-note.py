class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def Char_Counter(word):
            count_dict = defaultdict(int)
            for i in word:
                count_dict[i] += 1
            return count_dict
        
        ran = Char_Counter(ransomNote)
        mag = Char_Counter(magazine)
        
        for i in ran:
            if ran[i] > mag[i]:
                return False
        return True