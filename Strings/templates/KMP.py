def generate_lps(needle: str):
    n = len(needle)
    lps = [0] * n
    length = 0
    index = 1
    while index < n:
        if needle[length] == needle[index]:
            length += 1
            lps[index] = length
            index += 1
        else:
            if length == 0:
                index += 1
            else:
                length = lps[length - 1]
    return lps


def kmp(haystack: str, needle: str):
    h = len(haystack)
    n = len(needle)
    lps = generate_lps(needle)
    
    i = 0
    j = 0
    while i < h:
        if haystack[i] == needle[j]:
            if j == n - 1:
                return i - n + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
