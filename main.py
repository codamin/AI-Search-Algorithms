from agent import *
from foodProblem import *
from search import *

foodProblem = FoodSearchProblem('tests/test1.txt')

bfsAgent = Agent(foodProblem, generalSearch)
bfsAgent.search(searchType='bfs')

# idsAgent = Agent(foodProblem, ids)
# idsAgent.search(maxDepth = 50)


idsAgent = Agent(foodProblem, generalSearch)
idsAgent.search(searchType='aStar', heuristic = lambda x : 0)