import time
from utils import *

def getFringe(searchType):
    if searchType == 'bfs':
        return FringeBFS()
    elif searchType == 'dfs' or searchType == 'ids':
        return FringeDFS()
    elif searchType == 'aStar':
        return FringeAstar()

def generalSearch(problem, searchType, depthLimit = 30, h_n = lambda x : 0):
    fringe = getFringe(searchType)    
    visited = set()
    if searchType == 'aStar' : initialState = aStarNode(problem.startState, [])
    else: initialState = Node(problem.startState, [])
    
    fringe.push(initialState)
    
    while not fringe.isEmpty():
        selectedNode = fringe.pop()
        state, prevAccessPath = selectedNode.state, selectedNode.accessPath
        
        # Only for A* search
        if searchType == 'aStar':
            prevAccessCost = selectedNode.accessCost
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
                newNodeCost = prevAccessCost + newCost
                totalEval = newNodeCost + h_n(state)
                fringe.push(aStarNode(successor, newNodeAccessPath, newNodeCost, totalEval))
            else:
                fringe.push(Node(successor, newNodeAccessPath))

def ids(problem, maxDepth):
    for _ in range(maxDepth):
        foundPath = generalSearch(problem, 'ids', maxDepth)
        if foundPath is not None:
            return foundPath
    return None

# def dfs(problem):