class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        mention = [0]*n
        online = [1]*n
        events.sort(key = lambda x:(int(x[1]), x[0]!="OFFLINE"))
        
        for m, t, ids in events:
            if m=="OFFLINE":
                online[int(ids)] = int(t) + 60
            else:
                if ids!="HERE" and ids!="ALL":
                    for id in ids.split(" "):
                        id = int(id[2:])
                        mention[id] +=1
                elif ids == "ALL":
                    for i in range(n):
                        mention[i] += 1
                else:
                    for i in range(n):
                        if online[i]<=int(t):
                            mention[i] += 1
        return mention 