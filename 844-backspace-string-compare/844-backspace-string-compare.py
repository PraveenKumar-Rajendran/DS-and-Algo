class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
                
        def process_string(string):
            lenvar = len(string)
            return_list = []
            for i in string:
                if i == "#":
                    if return_list: return_list.pop() 

                else:
                    return_list.append(i)
            return return_list
        
        return True if process_string(s) == process_string(t) else False
    
    
    