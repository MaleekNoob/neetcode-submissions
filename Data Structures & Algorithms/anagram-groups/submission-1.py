from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        # print (anagram_map)
        
        for word in strs:
            # print('processing: ', word)
            anagram_key = "".join(sorted(word))
            # print('Anagram Key: ', anagram_key)
            anagram_map[anagram_key].append(word)
            # print('current condition of Anagram Map: ', anagram_map)
            
        # print('returning ANAGRAM MAP: ', anagram_map.values())
        return list(anagram_map.values())