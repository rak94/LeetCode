class DecodeWays:
    def decode_str_int(self, s: str) -> int:
        decSet = { len(s) : 1 }

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                decSet[i] = 0
            else:
                decSet[i] = decSet[i + 1]

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                decSet += [i + 2]

        return decSet[0]