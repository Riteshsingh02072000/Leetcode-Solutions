class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.strip().split()
        dictionary.sort()
        print(sentence)
        for i, x in enumerate(sentence):
            for z in dictionary:
                if x.startswith(z):

                    sentence[i] = z
                    break

        return " ".join(sentence)