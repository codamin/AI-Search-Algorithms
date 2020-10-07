import time
from utils import *

def getFringe(searchType):
    if searchType == 'bfs':
        return FringeBFS()
    elif searchType == 'dfs' or searchType == 'ids':
        return FringeDFS()
    elif searchType == 'aStar':
        return FringeAstar()

def generalSearch(problem, searchType, depthLimit = None, heuristic = lambda x:0):
    fringe = getFringe(searchType)    
    explored = set()
    fringe.push(problem.startState, [], g_n = 0, f_n = 0)

    while not fringe.isEmpty():
        state, path, g_n, _ = fringe.pop()
        # Only for IDS search
        if searchType == 'ids' and len(path) == depthLimit:
            continue

        if problem.isGoalState(state):
            return(path)

        if state in explored:
            continue
        explored.add(state)

        for successor, action, cost in problem.getSuccessors(state):
            child_path = path + [action]
            child_g_n = g_n + cost
            child_f_n = g_n + heuristic(state)
            # print(child_path, "@@@@@@@@@@@@@@@@@@@@@@@@")
            # if successor not in explored:
            fringe.push(successor, child_path, child_g_n, child_f_n)

def ids(problem, maxDepth):
    for _ in range(maxDepth):
        foundPath = generalSearch(problem, 'ids', maxDepth)
        if foundPath is not None:
            return foundPath
    return None

# def dfs(problem):