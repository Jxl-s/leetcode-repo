class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        team_count = (len(skill) // 2)
        
        if total_skill % team_count != 0:
            return -1
        
        target_skill = total_skill // team_count
        skill_dict = defaultdict(int)

        chemistry = 0
        for i, s in enumerate(skill):
            complement = target_skill - s
            if complement in skill_dict:
                skill_dict[complement] -= 1
                chemistry += s * complement

                if skill_dict[complement] == 0:
                    del skill_dict[complement]
            else:
                skill_dict[s] += 1
        
        if sum(skill_dict.values()) == 0:
            return chemistry
        else:
            return -1