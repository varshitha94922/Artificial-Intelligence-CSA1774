 start,end =[3,3,1],[0,0,0]
def do_action(state,action):
    if state[2] == 1:
        return [state[i] - action[i] for i in range(3)]
    else:
        return [state[i] + action[i] for i in range(3)]
def is_legal(state):
    if 0 <= state[0] <= 3 and 0 <= state[1] <= 3:
        return True
    else:
        return False
def is_bank_safe(bank):
    if bank[1] > bank[0] and bank[0] != 0:
        return False
    else:
        return True
def is_state_safe(state):
    other_bank = [start[i]-state[i] for i in range(3)]
    if is_bank_safe(state) and is_bank_safe(other_bank) :
        return True
    else:
        return False
def next_possible_actions(state):
    actions = [[1,0,1],[0,1,1],[1,1,1],[2,0,1],[0,2,1]]
    moves = []
    for i in actions:
        j =…
[10:30 AM, 9/21/2022] Neelima: from sys import maxsize
from itertools import permutations
V = 4
 

def travellingSalesmanProblem(graph, s):
 
    
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
   
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        
        current_pathweight = 0
 
       
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
       
        min_path = min(min_path, current_pathweight)
         
    return min_path
 
 

if _name_ == "_main_":
 
   
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
