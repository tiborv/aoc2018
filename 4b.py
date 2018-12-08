import sys

actions = []

for line in sys.stdin:
    info = line.split("]")
    datestr = info[0].split('1518-')[1]
    date = [
        datestr.split("-")[0], 
        datestr.split("-")[1].split(" ")[0],
        datestr.split(" ")[1].split(":")[0],
        datestr.split(" ")[1].split(":")[1]
        ]
    action = 0 if 'Guard' in info[1] else (1 if 'wakes' in info[1] else 2)
    actions.append({
        "action": action,
        "guard": info[1].split("#")[1].split(" ")[0] if action == 0 else None,
        "date": map(int, date)
    })
    
def sortFn(a, b):
    for i in xrange(4):
        if a["date"][i] > b["date"][i]:
            return 1
        if a["date"][i] < b["date"][i]:
            return -1
    return 0

actions.sort(sortFn)

def diffMins(a, b):
    hours = b["date"][2] - a["date"][2]
    mins = b["date"][3] - a["date"][3]
    return (hours * 60) + mins


guards = []
currGurad = {}
for i in xrange(len(actions)):
    if actions[i]["action"] == 0:
        existingGuards = [guard for guard in guards if guard["guard"] == currGurad["guard"]]
        if currGurad != {}:
            if len(existingGuards) == 0:
                guards.append(currGurad)
            else:
                guardId = existingGuards[0]["guard"]
                slept, sumsleep = [], 0
                for g in existingGuards:
                    slept += g["slept"]
                    sumsleep += g["sleep"]
                guards=filter(lambda g: g["guard"] != guardId, guards)
                guards.append({
                    "guard": guardId,
                    "sleep": sumsleep + currGurad["sleep"],
                    "slept": slept + currGurad["slept"]
                })
        
        currGurad = {
            "guard": actions[i]["guard"],
            "sleep": 0,
            "slept": []
        }
    if actions[i]["action"] == 2:
        currGurad["sleep"] += diffMins(actions[i], actions[i+1])
        currGurad["slept"].extend([actions[i]["date"], actions[i+1]["date"]])

maxSleptGuard = {
    "sleep": 0
}
for g in guards:
    if g["sleep"] > maxSleptGuard["sleep"]:
        maxSleptGuard = g

sleepintervals = maxSleptGuard["slept"]
slept = {}
for i in xrange(0, len(sleepintervals), 2):
    fr, to = (sleepintervals[i][2], sleepintervals[i][3]), (sleepintervals[i+1][2], sleepintervals[i+1][3])
    while fr != to:
        if fr[1] in slept:
            slept[fr[1]] += 1
        else:
            slept[fr[1]] = 1
        fr = (fr[0], fr[1] + 1)
        if fr[1] > 59:
            fr = (fr[0] + 1, 0)

print(int(maxSleptGuard["guard"]) * slept.keys()[slept.values().index(max(slept.values()))])