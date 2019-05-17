#тут больше приходится разбираться в графах а не с json
import json
data=json.loads('[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]')
data={obj['name']:obj['parents'] for obj in data}
def children(start,visited=None):
    if visited is None:
        visited = set()
    direct_children = list(c for c in data if start in data[c])
    visited.add(start)
    for next in direct_children:
        children(next, visited)
    return visited
for key in sorted(data.keys()):
    num_of_parents=len(children(key))
    print(key,":",str(num_of_parents))