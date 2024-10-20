class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, key):
        if self.parents[key] != key:
            self.parents[key] = self.find(self.parents[key])

        return self.parents[key]

    def union(self, a, b):
        self.parents[self.find(a)] = self.find(b)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(len(accounts))
        owners = {} # email -> owner

        for i in range(len(accounts)):
            owner = accounts[i][0]
            # go through aech email
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                # if email is already owned, link the owner
                if email in owners:
                    union_find.union(i, owners[email])

                owners[email] = i
        
        email_list = {}
        for email, owner in owners.items():
            key = union_find.find(owner)
            if key not in email_list: email_list[key] = []

            email_list[key].append(email)
        
        output = []
        for owner, emails in email_list.items():
            output.append([accounts[owner][0], *sorted(emails)])

        return output