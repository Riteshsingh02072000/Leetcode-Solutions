class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        l2r = sorted([(p, h, d, idx) for idx, (p, h, d) in enumerate(zip(positions, healths, directions))])
        stack = []

        for p, h, d, idx in l2r:
            if d == 'R':
                stack.append((idx, h, d))

            else:
                while stack and stack[-1][2] == 'R' and d == "L":
                    last_idx, last_h, last_d = stack.pop()
                    if last_h > h:
                        idx, h, d = last_idx, last_h - 1, "R"
                    elif last_h<h:
                        h, d = h-1, "L"
                    else:
                        d = "#"
                    
                if d != '#':
                    stack.append((idx, h, d))
        stack.sort()
        return [x[1] for x in stack]