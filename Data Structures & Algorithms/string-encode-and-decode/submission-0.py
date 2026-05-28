class Solution:

    def encode(self, strs: list[str]) -> str:
        encode = ''
        for word in strs:
            encode += (str(len(word)) + '#' + word)
        return encode
        

    def decode(self, s: str) -> list[str]:
        flag = 0
        start = 0
        main_str = []
        while s != []:
            if start >= len(s):
                break
            
            if s[start] == '#':
                num = s[flag: start]
                length = int(num)
                flag = start+1
                print('length: ', length)
                lower = flag + length
                word = s[flag: lower]
                main_str.append(word)
                s = s[lower:]
                flag = 0
                start = 0
            start += 1
            
        return main_str
