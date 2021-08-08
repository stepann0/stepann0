s = ")(){}"
parentheses = {"(":")", "[":"]", "{":"}", "<":">"}

def isValid(s: str) -> bool:
    opp = [i[-1] for i in parentheses.items()]
    if s[0] in opp or s[-1] in opp:
        return False
    for i in find_closed(s):
        start, stop = i[0], i[1]+1
        for p in parentheses:
            if s[start:stop].count(p) != s[start:stop].count(parentheses[p]):
                return False
    return True

def find_closed(s:str):
    res = []
    for i in range(len(s)):
        if s[i] in parentheses:
            for j in range(i, len(s)):
                if s[j] == parentheses[s[i]]:
                    res.append((i, j))
                    break
    return res

print(isValid(s))
