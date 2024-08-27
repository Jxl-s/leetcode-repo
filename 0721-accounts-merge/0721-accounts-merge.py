from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        all_accounts = {}
        for acc in accounts:
            if acc[0] in all_accounts:
                all_accounts[acc[0]].append(acc[1:])
            else:
                all_accounts[acc[0]] = [acc[1:]]
        
        output = []
        for name, accs in all_accounts.items():
            adj = {}
            for i, email_list in enumerate(accs):
                for email in email_list:
                    if email in adj:
                        adj[email].append(i)
                    else:
                        adj[email] = [i]
            
            # Start traversal
            visited = set()
            def dfs(email):
                if email in visited:
                    return []

                visited.add(email)
                all_emails = [email]
                for i in adj[email]:
                    for email in accs[i]:
                        all_emails.extend(dfs(email))

                return all_emails
            
            email_groups = []
            for email in adj.keys():
                result = dfs(email)
                if len(result) > 0:
                    email_groups.append(result)
            
            for group in email_groups:
                output.append([name, *sorted(group)])

        return output