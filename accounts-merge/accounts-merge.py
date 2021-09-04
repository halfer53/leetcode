class Name:
    def __init__(self, name):
        self.name = name
        self.email = set()
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = dict()
        for acc in accounts:
            name = acc[0]
            namecls = None
            for i in range(1, len(acc)):
                email = acc[i]
                if email in dic:
                    if namecls is not None and dic[email] != namecls:
                        person = dic[email]
                        namecls.email.update(person.email)
                        for p in person.email:
                            dic[p] = namecls
                    else:
                        namecls = dic[email]
            if namecls is None:
                namecls = Name(name)
            for i in range(1, len(acc)):
                email = acc[i]
                dic[email] = namecls
                namecls.email.add(email)
        ret = []
        names = set()
        for email, name in dic.items():
            if name not in names:
                names.add(name)
        for name in names:
            ret.append([name.name] + sorted(list(name.email)))
        return ret
        