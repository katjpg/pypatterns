class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = []
        
        for s in strs:
            # encode each word: length + "#" + word
            # "hello" -> "5#hello"
            encoded.append(str(len(s)) + "#" + s)
            
        # ["5#hello", "5#world"] -> "5#hello5#world"
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0 
        
        while i < len(s):
            j = i
            
            # move j until "#" is found
            while s[j] != "#":
                j += 1

            # i:j are the length digits
            # if s = "5#hello5#world", then s[i:j] = "5"
            length = int(s[i:j])

            # start after "#", then take 'length' characters
            word = s[j + 1:j + 1 + length]
            decoded.append(word)

            # move i -> start of the next encoded chunk
            i = j + 1 + length 
            
        return decoded

""" 
time: O(n)
- encode each char once.
- decode by iterating through encoded str once.

space: O(n)
- encoded str and decoded list grow with input size.

"""