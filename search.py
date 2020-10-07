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
    visited = set()
    fringe.push(problem.startState, [])

    while not fringe.isEmpty():
        selectedNode = fringe.pop()
        state, prevAccessPath = selectedNode[:2]
        # print(prevAccessPath)
        # Only for A* search
        if searchType == 'aStar':
            prevAccessCost = selectedNode[2]
        # Only for IDS search
        if searchType == 'ids' and len(prevAccessPath) == depthLimit:
            continue
        if problem.isGoalState(state):
            return(prevAccessPath)
        if state in visited:
            continue
        visited.add(state)

        for successor, action, newCost in problem.getSuccessors(state):
            newNodeAccessPath = prevAccessPath + [action]
            if searchType == 'aStar':
                g_n = prevAccessCost + newCost
                f_n = g_n + heuristic(state)
                fringe.push(successor, newNodeAccessPath, g_n, f_n)
            else:
                fringe.push(successor, newNodeAccessPath)

def ids(problem, maxDepth):
    for _ in range(maxDepth):
        foundPath = generalSearch(problem, 'ids', maxDepth)
        if foundPath is not None:
            return foundPath
    return None

# def dfs(problem):