import time
from utils import *

def getFringe(searchType):
    if searchType == 'bfs':
        return FringeBFS()
    elif searchType == 'dfs' or searchType == 'ids':
        return FringeDFS()
    elif searchType == 'aStar':
        return FringeAstar()

def solution(node, seenStates, distinctStates):
    sol = {}
    sol['total number of explored states'] = seenStates
    sol['total number of distinct found states'] = distinctStates
    state, parent, action, depth, g_n, f_n = node
    sol['solution depth'] = depth
    path = action
    while(parent[1] is not None):
        path = parent[2] + '-' + path
        parent = parent[1]
    sol['path'] = path
    return sol

def getHeuristic(problem, name):
    if name == 'one':
        return problem.h1
    if name == 'two':
        return problem.h2
    return lambda s : 0

def graphSearch(problem, searchType, depthLimit = None, heuristic = None):
    fringe = getFringe(searchType)    
    explored = set()
    fringe.push(problem.startState, parent = None, action = None, g_n = 0, f_n = 0, depth = 0)

    distinctStates = 0
    h_n = getHeuristic(problem, heuristic)

    while not fringe.isEmpty():
        node = fringe.pop()
        state, parent, action, depth, g_n, f_n = node
        # Only for IDS search
        if searchType == 'ids' and depth == depthLimit:
            continue

        if problem.isGoalState(state):
            return(solution(node, len(explored), distinctStates))
        # if state in explored:
        #         continue

        explored.add(state)

        for successor, action, cost in problem.getSuccessors(state):
            child_g_n = g_n + cost
            child_f_n = g_n + h_n(state)
            child_action = action
            child_depth = depth + 1
            
            if successor in explored:
                continue

            if fringe.push(successor, node, child_action, child_depth, child_g_n, child_f_n):
                distinctStates += 1

def ids(problem, maxDepth):
    for _ in range(maxDepth):
        foundPath = graphSearch(problem, 'ids', maxDepth)
        if foundPath is not None:
            return foundPath
    return None

# def dfs(problem):