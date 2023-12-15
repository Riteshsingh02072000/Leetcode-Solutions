class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for path in paths:
            city = path[1]
            good = True

            for others in paths:
                if city == others[0]:
                    good = False
                    break
            if good:
                return city
        return ""