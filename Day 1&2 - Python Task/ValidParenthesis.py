class Solution:
    def isValid(self, s: str) -> bool:
        store = {"{":"}","[":"]","(":")"}
        c = len(s)
        v = []
        for i in s:
            if i in store:
                v.append(i)
                if store[i] in s:
                    v.append(i)
                    s.replace(i,"")
                else:
                    break
        if len(v) == c:
            return True
        else:
            return False