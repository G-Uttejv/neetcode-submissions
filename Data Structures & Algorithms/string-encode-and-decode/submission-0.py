class Solution:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        """
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length
        return res

