class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.fi = 0
        self.body = collections.deque([[0,0]])
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.body[-1]
        dirt = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        dx, dy = dirt[direction]
        x += dx
        y += dy
        # print(direction, x, y, self.body)
        if not ( 0 <= x < self.height and 0 <= y < self.width):
            return -1
        if self.fi < len(self.food) and x == self.food[self.fi][0] and y == self.food[self.fi][1]:
            self.fi += 1
        else:
            self.body.popleft()
        for point in self.body:
            if x == point[0] and y == point[1]:
                return -1
        self.body.append([x, y])
        return self.fi
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)