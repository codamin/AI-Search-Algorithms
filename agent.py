import time

class Agent:
    def __init__(self, problem, searchFunction):
        self.searchFunction = searchFunction
        self.problem = problem
    
    def search(self, **kargs):
        tic = time.time()
        if 'heuristic' in kargs:
            actions = self.searchFunction(self.problem, kargs['searchType'], kargs['heuristic'])
        elif 'searchType' in kargs:
            actions = self.searchFunction(self.problem, kargs['searchType'])
        elif 'maxDepth' in kargs:
            actions = self.searchFunction(self.problem, kargs['maxDepth'])
        toc = time.time()
        print('path {} found in {} seconds'.format(actions, (toc-tic)))