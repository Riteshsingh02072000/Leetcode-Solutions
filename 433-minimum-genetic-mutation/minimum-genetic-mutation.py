class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        q = deque([(startGene, 0)])
        visited = set()

        while q:
            gene, oper = q.popleft()
            for i in range(8):
                for c in 'ACGT':
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene == endGene:
                        return oper + 1
                    elif new_gene in bank and new_gene not in visited:
                        q.append((new_gene, oper+1))
                        visited.add(new_gene)
        return -1