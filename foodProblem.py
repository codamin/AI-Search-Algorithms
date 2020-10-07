import numpy as np
from utils import *

class FoodSearchProblem:
    def __init__(self, filename):
        self.actions = ['U', 'D', 'R', 'L']

        with open(filename) as file:
            read_line = lambda : list(map(int, file.readline().split(',')))
            self.dim_y, self.dim_x = read_line()
            s_x, s_y = read_line()
            food_num = read_line()[0]
            # self.map = np.zeros((dim_x, dim_y))
            foods = []
            for _ in range(food_num):
                food_y, food_x, count = read_line()
                foods.append((food_y, food_x, count))
                # self.map[food_x][food_y] = count
            self.startState = State([(s_y, s_x)], foods)

    def getCost(self):
        return 1

    def makeTransition(self, state, action):
        snake = state.snake.copy()
        foods = state.foods.copy()

        current_x = snake[0][1]        
        current_y = snake[0][0]
        
        newHead = None
        head = snake[0]

        if action == 'U':
            if current_y == 0:
                newHead = (self.dim_y - 1, head[1])
            else:
                newHead = (head[0] - 1, head[1])

        if action == 'D':
            if current_y == self.dim_y - 1:
                newHead = (0, head[1])
            else:
                newHead = (head[0] + 1, head[1])

        if action == 'R':
            if current_x ==  self.dim_x - 1:
                newHead = (head[0], 0)
            else:
                newHead = (head[0], head[1] + 1)
            
        if action == 'L':
            if current_x == 0:
                newHead = (head[0], self.dim_x - 1)
            else:
                newHead = (head[0], head[1] - 1)
        
        if newHead in snake:
            return None

        assert(newHead[0] >= 0 and newHead[0] <= self.dim_y)
        assert(newHead[1] >= 0 and newHead[1] <= self.dim_x)

        snake.insert(0, newHead)

        if self.hasFood(foods, newHead):
            self.eatFood(foods, newHead)
        else:
            snake.pop()

        return State(snake, foods)

    def hasFood(self, foods, position):
        return position in [(x,y) for (x,y,_) in foods]
    
    def eatFood(self, foods, position):
        for idx, food in enumerate(foods):
            if(food[0], food[1]) == position:
                if food[2] == 1:
                    foods.pop(idx)
                else:
                    foods[idx] = (food[0], food[1], food[2] - 1)

    def isGoalState(self, state):
        return len(state.foods) == 0

    def getSuccessors(self, state):
        successors = []
        for action in self.actions:
            suc = self.makeTransition(state, action)
            if suc is not None:
                successors.append((suc, action, self.getCost()))
        return successors
    
    def h1(self, state):
        ## return total foods remaining
        return sum([count for y,x,count in state.foods])

    def h2(self, state):
        ## return manhatan distance
        return sum(list(map(lambda f : min(self.dim_x - f[1], f[1]) +
            min(self.dim_y - f[0], f[0]), state.foods)))

class State:
    def __init__(self, snake, foods):
        self.snake = snake
        self.foods = foods
    
    def __str__(self):
        return("{} ## {}".format(self.snake, self.foods))

    def __hash__(self):
        return 51 * hash((tuple(self.snake))) +  17 * hash(tuple(self.foods))

    def __eq__(self,other):
        return self.snake == other.snake and self.foods == other.foods