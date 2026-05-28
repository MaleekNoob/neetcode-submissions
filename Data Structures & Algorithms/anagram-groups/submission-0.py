from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_set = set(strs)
        groupList = []
        for word in word_set:
            if strs == []:
                break
            # print('GAME STARTED!', strs)
            sub_list = []
            # print('processing ', word)
            found_indexes = []
            for i, candidate in enumerate(strs):
                # print('processing index: ', i, ' with value: ', candidate)
                if Counter(candidate) == Counter(word):
                    # print("MATCH FOUND - ", candidate)
                    sub_list.append(candidate)
                    # print('updated sub-list: ', sub_list)
                    found_indexes.append(i)
                    # print('updated found index list: ', found_indexes)
                    
            # print('deleting the following indexes: ')
            for index in reversed(found_indexes):
                print(index, " - ", strs[index])
                strs.pop(index)
                
            if sub_list == []:
                continue
                
            groupList.append(sub_list)
            
        return groupList